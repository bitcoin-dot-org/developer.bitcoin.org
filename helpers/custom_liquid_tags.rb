class HighlightTag < Liquid::Block
  def initialize(_tag, params, _tokens)
    super
    @language = params
  end

  def render(context)
    output = ".. highlight:: #{@language}\n"
    code = super.to_s
    code.each_line do |line|
      output += "    " + line
    end
    output
  end
end

# This class is based on code from https://github.com/bitcoin/bitcoin.org
# licensed unter the MIT License (MIT) available on
# http://opensource.org/licenses/MIT.
class AutocrossrefTag < Liquid::Block
  def render(context)
    output = super

    ## Load terms from file only if we haven't loaded them before
    site = context.registers[:site]
    if !site.has_key?("crossref_loaded")
      ## Load refs from file and then downcase them all so we can
      ## easily detect when we define xrefs more than once
      mixed_case_refs = YAML.load_file("_autocrossref.yaml")
      unvalidated_refs = Hash.new
      mixed_case_refs.each { |key, value|
        unvalidated_refs[key.to_s.downcase] = value.to_s.downcase
      }

      if site.has_key?("crossref")
        ## We already have refs loaded, so merge
        site['crossref'].merge!(unvalidated_refs) {
          |key, old_value, new_value|

          if old_value != new_value
            abort("Error: autocrossref key '#{key}' wants to point to both '#{old_value}' and '#{new_value}'")
          end

          new_value
        }
      else
        ## We don't have refs loaded yet, so copy
        site['crossref'] = unvalidated_refs
      end
      site['crossref_loaded'] = true
    end


    ## Sort terms by reverse length, so longest matches get linked
    ## first (e.g. "block chain" before "block"). Otherwise short
    ## terms would get linked first and there'd be nothing for long
    ## terms to link to.
    site['crossref'].sort_by { |k, v| -k.length }.each { |term|

      term[1] = term[0] if term[1].nil? || term[1].empty?

      term[0] = Regexp.escape(term[0])

      ## Replace literal space with \s to match across newlines. This
      ## can do weird things if you don't end sentences with a period,
      ## such as linking together "standard" and "transactions" in
      ## something like this:
      ### * RFC1234 is a standard
      ###
      ### Transactions are cool
      term[0].gsub!('\ ', '\s+')

      output.gsub!(/
          (?<!\w)  ## Don't match inside words
          #{term[0]}('s)?  ## Find our key
          (?![^\[]*\])  ## No subst if key inside [brackets]
          (?![^\{]*\})  ## No subst if key inside {braces}
          (?![^\s]*<!--noref-->)  ## No subst if <!--noref--> after key
          (?!((?!<pre>).)*(<\/pre>))  ## No subst on a line with a closing pre tag. This
                                      ## prevents matching in {% highlight %} code blocks.
          (?![^\(]*(\.svg|\.png|\.gif))  ## No subst if key inside an image name. This
            ## simple regex has the side effect that we can't
            ## use .svg, .png, or .gif in non-image base text; if that
            ## becomes an issue, we can devise a more complex
            ## regex
          (?!\w)  ## Don't match inside words
          (?!.*(<\/h{1-6}>))  ## Don't match inside words
          (?!`)   ## Don't match strings ending with a tic, unless the xref itself ends with a tic
        /xmi) {|s|
            if term[1] == "do not autocrossref"
                s.gsub(/( |$)/, "<!--noref-->\\&")
            else
                "[#{s.gsub(/`/, '"')}][#{term[1]}]"
            end
            }
    }
    output.gsub!(/<!--.*?-->/m,'')  ## Remove all HTML comments

    output
  end
end

class IncludeTag < Liquid::Tag
  def initialize(_tag, params, _tokens)
    super
    params.strip!
    processed_params = ["bitcoin-core/bitcoin-core-possible-problems.md",
        "helpers/summaries.md", "helpers/vars.md"]
    ignored_params = ["helpers/subhead-links.md", "helpers/hero-social.html"]
    if processed_params.include?(params)
      @included_file = params
    elsif !ignored_params.include?(params)
      STDERR::puts "Warning: Unknown include '#{params}'"
    end
  end

  def render(context)
    if @included_file
      path = File.join(context.registers[:base_dir], "_includes", @included_file)
      included_content = File.read(path)
      template = Liquid::Template.parse(included_content)
      template.render
    end
  end
end

class IncludeAbsoluteTag < Liquid::Tag
  def initialize(_tag, params, _tokens)
    super
    params.strip!
    @included_file = params.split[1]
  end

  def render(context)
    if @included_file
      path = File.join(context.registers[:base_dir], @included_file)
      included_content = File.read(path)
      template = Liquid::Template.parse(included_content)
      template.render(nil, {registers:{
        site: {},
        base_dir: context.registers[:base_dir]
      }})
    end
  end
end

class InlineTemplateBlock < Liquid::Block
  def initialize(tag_name, text, tokens)
    super
    @template_name = '_templates/' + text.gsub(' ','') + '.inline'
  end

  def render(context)
    output = super

    data = YAML.load(output)
    path = File.join(context.registers[:base_dir], @template_name)
    @mytemplate = Liquid::Template.parse(File.read(path))
    @mytemplate.render('entry' => data)
  end
end

Liquid::Template.register_tag('highlight', HighlightTag)
Liquid::Template.register_tag('autocrossref', AutocrossrefTag)
Liquid::Template.register_tag('include', IncludeTag)
Liquid::Template.register_tag('include_absolute', IncludeAbsoluteTag)
Liquid::Template.register_tag('itemplate', InlineTemplateBlock)
