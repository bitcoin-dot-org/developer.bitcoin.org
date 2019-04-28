class Importer
  attr_accessor :base_dir, :target_base_dir

  def render_template(filename)
    source = File.read(filename)
    # TODO: Import and convert references
    source += "\n" + File.read("_references.md")
    source += "\n" + File.read("_glossary_references.md")
    template = Liquid::Template.parse(source)
    template.render(nil, {registers:{
      site: {},
      base_dir: base_dir
    }})
  end

  def import_file(source_file, target_file, title)
    print "Importing #{source_file} as #{target_file}"
    if title
      print " under title #{title}"
    end
    puts

    source_path = File.join(base_dir, source_file)
    target_path = File.join(target_base_dir, target_file)

    rendered = render_template(source_path)

    # Replace backticks by regular quotes because RST can't handle this kind
    # of nested markup
    rendered.gsub!(/\[\`(.*?)\`\]/, '["\1"]')

    rendered.gsub!(/\{:#term.*\}\{:\.term\}/,'')

    # Convert Markdown to reStructuredText
    Open3.popen2("pandoc -f markdown -t rst --wrap none") do |i,o,t|
      i.print rendered
      i.close

      converted = o.read

      if title
        # Prepend title to document so Sphinx puts it into the table of contents
        converted = title + "\n" + "-" * title.length + "\n\n" + converted
      end

      # Remove trailing `?` from path of images
      converted.gsub!(/\.\. figure:: (.+)\?/, '.. figure:: \1')
      converted.gsub!(/\.\.(.*)image:: (.+)\?/, '..\1image:: \2')

      converted.gsub!(/{:.no_toc}/, '')
      converted.gsub!(/{:.ntpd}/, '')

      File.write(target_path, converted)
    end
  end

  def import_sections(sections)
    sections.each do |section|
      source_dir = section[:source_dir]
      target_dir = section[:target_dir]
      section[:pages].each do |page, title|
        source_file = File.join(source_dir, page + ".md")
        target_file = File.join(target_dir, page + ".rst")
        import_file(source_file, target_file, title)
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

    File.open(File.join(target_base_dir, "_glossary_references.md"), "w") do |file|
      sorted_terms.each do |term, data|
        file.puts "[/en/glossary/#{term}]: ../reference/glossary.html##{term}"
      end
    end
  end
end
