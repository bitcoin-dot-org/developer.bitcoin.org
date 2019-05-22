require_relative "post_processor_rst"

class Importer
  attr_accessor :base_dir, :target_base_dir

  def initialize(tmp_rst_path = nil)
    @tmp_rst_path = tmp_rst_path
    @post_processor_rst = PostProcessorRst.new
  end

  def report_links()
    @post_processor_rst.report_links
  end

  def report_unrecognized_links()
    @post_processor_rst.report_unrecognized_links
  end

  def read_summaries()
    tr_file = File.join(base_dir, "_translations", "en.yml")
    tr = YAML.load_file(tr_file)
    @summaries = {
      "devguide/block_chain" => tr["en"]["blockchain-guide"]["summary"],
      "devguide/transactions" => tr["en"]["transactions-guide"]["summary"],
      "devguide/contracts" => tr["en"]["contracts-guide"]["summary"],
      "devguide/wallets" => tr["en"]["wallets-guide"]["summary"],
      "devguide/payment_processing" => tr["en"]["payment-processing-guide"]["summary"],
      "devguide/operating_modes" => tr["en"]["operating-modes-guide"]["summary"],
      "devguide/p2p_network" => tr["en"]["p2p-network-guide"]["summary"],
      "devguide/mining" => tr["en"]["mining-guide"]["summary"],
    }
  end

  def process_references(references)
    processed = ""
    references.each_line do |line|
      if line.start_with?("[bcc contribute code]")
        line = ""
      elsif line =~ /\[rpc (.*)\]:/
        command = $1
        line = "[rpc #{command}]: ../reference/rpc/#{command}.html\n"
      elsif line =~ /\[(.*) message\]: .* "(.*)"/
        message = $1
        summary = $2
        line = "[#{message} message]: ../reference/p2p_networking.html##{message} \"#{summary}\"\n"
      end
      processed += line
    end
    processed += "\n"
  end

  def read_references()
    @references = ""
    references = File.read(File.join(base_dir, "_includes", "references.md"))
    @references = process_references(references)
  end

  def show_references()
    puts @references
  end

  def render_template(filename)
    source = File.read(filename)
    source += "\n" + @references
    template = Liquid::Template.parse(source)
    template.render(nil, {registers:{
      site: {},
      base_dir: base_dir
    }})
  end

  def post_process_markdown(markdown, remove_divs: false)
    processed = ""
    markdown.each_line do |line|
      # Remove divs if requested
      next if remove_divs && (line.include?("<div") or line.include?("</div>"))

      # Replace backticks by regular quotes because RST can't handle this kind
      # of nested markup
      line.gsub!(/\[\`(.*?)\`(.*?)\]/, '["\1"\2]')

      # Remove term attributes because we currently don't support them in der
      # converted help
      line.gsub!(/\{:#term.*\}\{:\.term\}/,'')

      # Fix up header consistency
      if line == "#### Orphan Blocks\n"
        line = "### Orphan Blocks\n"
      end

      processed += line
    end
    processed
  end

  def import_file(source_file, target_file, title, summary, remove_divs: false)
    print "Importing #{source_file} as #{target_file}"
    if title
      print " under title #{title}"
    end
    puts

    source_path = File.join(base_dir, source_file)
    target_path = File.join(target_base_dir, target_file)

    rendered = render_template(source_path)

    rendered = post_process_markdown(rendered, remove_divs: remove_divs)

    if @tmp_rst_path
      File.write(File.join(@tmp_rst_path, target_file.sub(".rst", ".md")), rendered)
    end

    # Convert Markdown to reStructuredText
    Open3.popen2("pandoc -f markdown -t rst --wrap none") do |i,o,t|
      i.print rendered
      i.close

      converted = o.read

      if @tmp_rst_path
        File.write(File.join(@tmp_rst_path, target_file), converted)
      end

      converted = @post_processor_rst.run(converted, title: title, summary: summary)

      File.write(target_path, converted)
    end
  end

  def import_sections(sections)
    sections.each do |section|
      source_dir = section[:source_dir]
      target_dir = section[:target_dir]
      remove_divs = target_dir == "devguide"
      section[:pages].each do |page, title|
        source_file = File.join(source_dir, page + ".md")
        target_file = File.join(target_dir, page + ".rst")
        summary = @summaries["#{target_dir}/#{page}"]
        import_file(source_file, target_file, title, summary, remove_divs: remove_divs)
      end
    end
  end

  def import_images
    image_dir = File.join(base_dir, "img")
    target_image_dir = File.join(target_base_dir, "img")
    ["dev", "full-node"].each do |dir|
      Dir.entries(File.join(image_dir, dir)).each do |entry|
        next if entry.start_with?(".")

        source_path = File.join(image_dir, dir, entry)
        next if File.directory?(source_path)

        target_path = File.join(target_image_dir, dir, entry)

        FileUtils.cp(source_path, target_path)
      end
    end
  end

  def import_glossary
    terms = {}
    Dir.glob(File.join(base_dir, "_data/glossary/en/*.yaml")).each do |yaml_file|
      term = File.basename(yaml_file, ".yaml")
      data = {}

      yaml = YAML.load_file(yaml_file)

      data[:title] = yaml["required"]["title_max_40_characters_no_formatting"]
      data[:summary] = yaml["required"]["summary_max_255_characters_no_formatting"]
      data[:synonyms] = yaml["required"]["synonyms_shown_in_glossary_capitalize_first_letter"]
      data[:not_to_be_confused_withs] = yaml["optional"]["not_to_be_confused_with_capitalize_first_letter"]

      terms[term] = data
    end

    sorted_terms = terms.sort { |a,b| a <=> b }

    File.open(File.join(target_base_dir, "glossary.rst"), "w") do |file|
      file.puts "Glossary\n========"
      file.puts
      file.puts ".. glossary::"
      file.puts
      sorted_terms.each do |term, data|
        if data[:synonyms].empty?
          STDERR.puts "WARNING: No synonyms: #{term}"
        end
        data[:synonyms].each do |synonym|
          file.puts "  " + synonym
        end
        file.puts "    " + data[:summary]
        file.puts
        if data[:not_to_be_confused_withs]
          file.puts "    **Not to be confused with:** " + data[:not_to_be_confused_withs].join(", ")
          file.puts
        end
      end
    end

    sorted_terms.each do |term, data|
      @references += "[/en/glossary/#{term}]: glossary##{term}\n"
    end
  end

  def render_terms(terms)
    texts = {}
    terms.keys.each do |term|
      term =~ /<\/en\/(.*)#(.*)>/
      section = $1
      anchor = $2

      text = "#{anchor} (#{section}) (`original target <https://bitcoin.org/en/#{section}##{anchor}>`__)"

      texts[anchor] = text
    end

    out = ""
    texts.keys.sort.each do |term|
      out += ".. _#{term}:\n\n"
      out += texts[term] + "\n\n"
    end
    out
  end

  def write_terms_page()
    File.open(File.join(target_base_dir, "terms.rst"), "w") do |file|
      file.puts(":orphan:\n\n")
      file.puts("Terms\n=====\n\n")
      file.puts(".. note:: This is a temporary page with references used as " +
        "targets for links in the documentation. They should be replaced by " +
        "adding proper labels inline in the respective pages. This is more " +
        "easily be done manually so this page acts as a temporary placeholder " +
        "for that until the automatic import and conversion to RST is completed.\n\n")

      file.puts(render_terms(@post_processor_rst.tbd))
    end
  end
end
