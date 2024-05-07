require_relative "table_fixer"

class PostProcessorRst
  attr_reader :tbd

  def initialize()
    @regexp_link = /`([^`<]*?) <([^`>]*?)>`__/
    @links = {}
    @unrecognized_links = {}
    @tbd = {}
  end

  def increment_link_count(hash, text, target)
    key = "<#{target}> #{text}"

    if hash.has_key?(key)
      hash[key] += 1
    else
      hash[key] = 1
    end
  end

  def print_links_hash(hash, prefix=nil)
    hash.keys.sort.each do |link|
      if prefix
        print "#{prefix}: "
      end
      puts "#{link}: #{hash[link]}"
    end
  end

  def replace_glossary_link(text, target)
    target =~ /glossary#(.*)/
    term = $1

    if !term
      STDERR.puts("Warning: unable to parse glossary target: '#{target}'")
      return "`#{text} <#{target}>`"
    end

    term = term.gsub("-", " ")

    substitutions = {
      "unspent transaction output" => "utxo",
      "sighash all" => "sighash_all",
      "sighash none" => "sighash_none",
      "sighash single" => "sighash_single",
      "sighash anyonecanpay" => "sighash_anyonecanpay",
      "high priority transaction" => "high-priority transaction",
      "malleability" => "transaction malleability",
      "master chain code and private key" => "master chain code"
    }
    if substitutions.has_key?(term)
      term = substitutions[term]
    end

    if term != text
      term = "#{text} <#{term}>"
    end

    ":term:`#{term}`"
  end

  def replace_guide_link(text, target)
    target =~ /\/en\/(.*)-guide#?(.*)/
    guide = $1
    anchor = $2

    if anchor.start_with?("term-")
      increment_link_count(@tbd, text, target)
      return ":ref:`#{text} <#{anchor}>`"
    end

    processed_target = "../devguide/#{guide.gsub("-", "_")}.html"

    if !anchor.empty?
      processed_target += "#" + anchor
    end

    "`#{text} <#{processed_target}>`__"
  end

  def replace_reference_link(text, target)
    target =~ /\/en\/developer-reference#?(.*)/
    anchor = $1

    if anchor && anchor.start_with?("term-")
      increment_link_count(@tbd, text, target)
      return ":ref:`#{text} <#{anchor}>`"
    end

    map = {
      "remote-procedure-calls-rpcs" => "rpc/index.html",
      "wallets" => "wallets.html",
      "serialized-blocks" => "block_chain.html#serialized-blocks",
      "raw-transaction-format" => "transactions.html#raw-transaction-format",
      "protocol-versions" => "p2p_networking.html#protocol-versions",
      "not-a-specification" => "intro.html#not-a-specification",
      "message-headers" => "p2p_networking.html#message-headers",
      "merkle-trees" => "block_chain.html#merkle-trees",
      "getblocktxn" => "p2p_networking.html#getblocktxn",
      "cmpctblock" => "p2p_networking.html#cmpctblock",
      "blocktxn" => "p2p_networking.html#blocktxn",
      "block-headers" => "block_chain.html#block-headers",
      "compactsize-unsigned-integers" => "transactions.html#compactsize-unsigned-integers"
    }

    path = nil
    if map.has_key?(anchor)
      path = map[anchor]
    else
      if anchor == "signature_script_modification_warning"
        increment_link_count(@tbd, text, target)
        return ":ref:`#{text} <signature_script_modification_warning>`"
      else
        record_unrecognized_link(text, target)
      end
    end

    if path
      processed_target = "../reference/#{path}"
    else
      processed_target = target
    end

    "`#{text} <#{processed_target}>`__"
  end

  def replace_examples_link(text, target)
    target =~ /\/en\/developer-examples#?(.*)/
    anchor = $1

    if anchor && anchor.start_with?("term-")
      increment_link_count(@tbd, text, target)
      return ":ref:`#{text} <#{anchor}>`"
    end

    map = {
      "complex-raw-transaction" => "transactions.html#complex-raw-transaction",
      "simple-raw-transaction" => "transactions.html#simple-raw-transaction",
      "" => "index.html",
      "payment-protocol" => "payment_processing.html#payment-protocol",
      "parsing-a-merkleblock" => "p2p_networking.html#parsing-a-merkleblock",
      "creating-a-bloom-filter" => "p2p_networking.html#creating-a-bloom-filter"
    }

    path = nil
    if map.has_key?(anchor)
      path = map[anchor]
    else
      if anchor == "signature_script_modification_warning"
        increment_link_count(@tbd, text, target)
      else
        record_unrecognized_link(text, target)
      end
    end

    if path
      processed_target = "../examples/#{path}"
    else
      processed_target = target
    end

    "`#{text} <#{processed_target}>`__"
  end

  def process_link(link)
    link =~ @regexp_link
    text = $1
    target = $2

    increment_link_count(@links, text, target)

    if target.start_with?("glossary#")
      replace_glossary_link(text, target)
    elsif target =~ /\/en\/.*-guide/
      replace_guide_link(text, target)
    elsif target =~ /\/en\/developer-examples/
      replace_examples_link(text, target)
    elsif target =~ /\/en\/developer-reference/
      replace_reference_link(text, target)
    elsif target == "#avoiding-key-reuse"
      "`#{text} <../devguide/transactions.html#avoiding-key-reuse>`__"
    elsif target =~ /\/en\/release\/(.*)/
      "`#{text} <https://bitcoin.org/en/release/#{$1}>`__"
    elsif target =~ /\/en\/download/
      "`#{text} <https://bitcoin.org/en/download>`__"
    elsif target =~ /\/en\/development(.*)/
      "`#{text} <https://bitcoin.org/en/development#{$1}>`__"
    elsif target == "/en/alert/2013-03-11-chain-fork"
      "`#{text} <https://bitcoin.org/en/alert/2013-03-11-chain-fork>`__"
    elsif target.start_with?("http")
      # External links, taken as they are
      link
    elsif target.start_with?("../")
      # Internal links generated when importing the references in
      # Importer.read_references
      link
    else
      record_unrecognized_link(text, target)
      link
    end
  end

  def record_unrecognized_link(text, target)
    STDERR.puts "Unrecognized link: `#{text} <#{target}>`"
    increment_link_count(@unrecognized_links, text, target)
  end

  def run(rst, title: nil, summary: nil)
    processed = ""

    preamble = ""

    if title
      # Prepend title to document so Sphinx puts it into the table of contents
      preamble += title + "\n" + "=" * title.length + "\n\n"
    end

    if summary
      preamble += summary + "\n\n"
    end

    processed = preamble + rst

    # Remove trailing `?` from path of images
    processed.gsub!(/\.\. figure:: (.+)\?/, '.. figure:: \1')
    processed.gsub!(/\.\.(.*)image:: (.+)\?/, '..\1image:: \2')

    processed.gsub!(/{:.no_toc}/, '')
    processed.gsub!(/{:.ntpd}/, '')

    processed.gsub!(@regexp_link) do |match|
      process_link(match)
    end

    processed = TableFixer.new.fixup_tables(processed)

    processed
  end

  def report_links()
    print_links_hash(@links)
  end

  def report_unrecognized_links()
    print_links_hash(@unrecognized_links)
  end
end
