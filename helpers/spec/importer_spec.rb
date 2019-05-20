require_relative 'spec_helper'

describe Importer do
  describe "#post_process_markdown" do
    it "keeps plain text" do
      text = "One line\nsecond line\nLast\n"
      expect(subject.post_process_markdown(text)).to eq(text)
    end

    it "replaces backticks" do
      markdown = '[`abc`]'
      expected = '["abc"]'
      expect(subject.post_process_markdown(markdown)).to eq(expected)
    end

    it "removes terms" do
      markdown = "x{:#term-fork}{:.term}y"
      expected = "xy"
      expect(subject.post_process_markdown(markdown)).to eq(expected)
    end

    it "removes HTML divs" do
      markdown = <<EOT
one
<div class="toccontent-block toccontent-intro" markdown="block">
two
</div>
three
EOT
      expected = <<EOT
one
two
three
EOT
      expect(subject.post_process_markdown(markdown)).to eq(markdown)
      expect(subject.post_process_markdown(markdown,remove_divs: true)).to eq(expected)
    end
  end

  describe "#process_references" do
    it "processes references" do
      references = <<EOT
{% comment %}<!-- Terms; must have tooltip description in "quotes"; alphabetical order -->{% endcomment %}
[bitcoin URI]: /en/payment-processing-guide#term-bitcoin-uri "A URI ..."

{% comment %}<!-- RPCs; alphabetical order -->{% endcomment %}
[rpc abandontransaction]: /en/developer-reference#abandontransaction
[rpc addmultisigaddress]: /en/developer-reference#addmultisigaddress

{% comment %}<!-- P2P protocol messages; alphabetical order -->{% endcomment %}
[addr message]: /en/developer-reference#addr "The P2P network message which relays IP ..."
[alert message]: /en/developer-reference#alert "The P2P network message which sends alerts ..."

[bcc contribute code]: /{{page.lang}}/{% translate development url %}
[bcc contribute documentation]: /en/bitcoin-core/contribute/documentation
EOT
      expected = <<EOT
{% comment %}<!-- Terms; must have tooltip description in "quotes"; alphabetical order -->{% endcomment %}
[bitcoin URI]: /en/payment-processing-guide#term-bitcoin-uri "A URI ..."

{% comment %}<!-- RPCs; alphabetical order -->{% endcomment %}
[rpc abandontransaction]: ../reference/rpc/abandontransaction.html
[rpc addmultisigaddress]: ../reference/rpc/addmultisigaddress.html

{% comment %}<!-- P2P protocol messages; alphabetical order -->{% endcomment %}
[addr message]: ../reference/p2p_networking.html#addr "The P2P network message which relays IP ..."
[alert message]: ../reference/p2p_networking.html#alert "The P2P network message which sends alerts ..."

[bcc contribute documentation]: /en/bitcoin-core/contribute/documentation

EOT
      expect(subject.process_references(references)).to eq(expected)
    end
  end

  describe "#render_terms" do
    it "renders terms" do
      terms = {
        "</en/developer-examples#term-pp-pki-data> PKI data" => 1,
        "</en/payment-processing-guide#term-bitcoin-uri> “bitcoin:” URI" => 9,
        "</en/developer-reference#signature_script_modification_warning> signature script modification warning" => 1,
        "</en/payment-processing-guide#term-bitcoin-uri>  URI" => 1
      }
      expected = <<EOT
.. _signature_script_modification_warning:

signature_script_modification_warning (developer-reference) (`original target <https://bitcoin.org/en/developer-reference#signature_script_modification_warning>`__)

.. _term-bitcoin-uri:

term-bitcoin-uri (payment-processing-guide) (`original target <https://bitcoin.org/en/payment-processing-guide#term-bitcoin-uri>`__)

.. _term-pp-pki-data:

term-pp-pki-data (developer-examples) (`original target <https://bitcoin.org/en/developer-examples#term-pp-pki-data>`__)

EOT
      expect(subject.render_terms(terms)).to eq(expected)
    end
  end
end
