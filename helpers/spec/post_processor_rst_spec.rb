require_relative 'spec_helper'

describe PostProcessorRst do
  describe "#run" do
    it "adds title" do
      text = "sometext\n"
      title = "Title"
      expected = <<EOT
Title
=====

sometext
EOT
      expect(subject.run(text, title: title)).to eq(expected)
    end

    it "adds summary" do
      text = "sometext\n"
      summary = "Summary"
      expected = <<EOT
Summary

sometext
EOT
      expect(subject.run(text, summary: summary)).to eq(expected)
    end

    it "removes trailing ? from image links" do
      rst = <<EOT
.. |Warning icon| image:: /img/icons/icon_warning.svg?
.. figure:: /img/dev/en-hd-tree.svg?
Question?
EOT
      expected = <<EOT
.. |Warning icon| image:: /img/icons/icon_warning.svg
.. figure:: /img/dev/en-hd-tree.svg
Question?
EOT
      expect(subject.run(rst)).to eq(expected)
    end

    it "removes unneeded attributes" do
      rst = <<EOT
{:.no_toc}
{:.ntpd}
text
EOT
      expected = <<EOT


text
EOT
      expect(subject.run(rst)).to eq(expected)
    end

    it "replaces glossary links" do
      rst = <<EOT
`network </en/developer-guide#term-network>`__ in `consensus <glossary#consensus>`__. Called `consensus rules <glossary#consensus-rules>`__.
`transaction identifiers (TXIDs) <glossary#txid>`__
EOT
            expected = <<EOT
:ref:`network <term-network>` in :term:`consensus`. Called :term:`consensus rules`.
:term:`transaction identifiers (TXIDs) <txid>`
EOT
      expect(subject.run(rst)).to eq(expected)
    end
  end

  describe "#replace_glossary_link" do
    it "replaces single word term" do
      expect(subject.replace_glossary_link("abc", "glossary#abc")).to eq(":term:`abc`")
    end

    it "replaces multiple word term" do
      expect(subject.replace_glossary_link("abc de f", "glossary#abc-de-f")).to eq(":term:`abc de f`")
    end

    it "replaces term with alt text" do
      expect(subject.replace_glossary_link("xy z", "glossary#abc")).to eq(":term:`xy z <abc>`")
    end
  end

  describe "#replace_guide_link" do
    it "replaces guide links" do
      tests = [
        ["a b", "/en/wallets-guide", "a b", "../devguide/wallets.html"],
        ["c d", "/en/wallets-guide#hardened-keys", "c d", "../devguide/wallets.html#hardened-keys"],
        ["e", "/en/wallets-guide#hardened-keys", "e", "../devguide/wallets.html#hardened-keys"],
        ["g", "/en/transactions-guide#avoiding-key-reuse", "g", "../devguide/transactions.html#avoiding-key-reuse"],
        ["h", "/en/p2p-network-guide", "h", "../devguide/p2p_network.html"]
      ]
      tests.each do |test|
        expect(subject.replace_guide_link(test[0], test[1])).to eq("`#{test[2]} <#{test[3]}>`__")
      end
    end

    it "replaces term links" do
      expect(subject.replace_guide_link("f", "/en/wallets-guide#term-xyz")).to eq(":ref:`f <term-xyz>`")
    end
  end

  describe "#replace_reference_link" do
    it "replaces reference links" do
      tests = [
        ["x", "/en/developer-reference#wallets", "x", "../reference/wallets.html"]#,
#        ['"version" message', "en/developer-reference#version", '"version" message', "../reference/p2p_networking.html#version"],
#        ['“signrawtransaction”', "/en/developer-reference#signrawtransaction", '“signrawtransaction”', "../reference/rpc/sendrawtransaction.html"]
      ]
      tests.each do |test|
        expect(subject.replace_reference_link(test[0], test[1])).to eq("`#{test[2]} <#{test[3]}>`__")
      end
    end

    it "replaces term links" do
      expect(subject.replace_reference_link("f", "/en/developer-reference#term-v2-block")).to eq(":ref:`f <term-v2-block>`")
    end
  end

  describe "#process_link" do
    it "replaces release links" do
      expect(subject.process_link("`Bitcoin Core 0.14.2 </en/release/v0.14.2>`__"))
        .to eq("`Bitcoin Core 0.14.2 <https://bitcoin.org/en/release/v0.14.2>`__")
    end

    it "replaces download link" do
      expect(subject.process_link("`Bitcoin Core </en/download>`__"))
        .to eq("`Bitcoin Core <https://bitcoin.org/en/download>`__")
    end

    it "replaces developer communities link" do
      expect(subject.process_link("`X </en/development#dev-communities>`__"))
        .to eq("`X <https://bitcoin.org/en/development#dev-communities>`__")
    end
  end
end
