require_relative 'spec_helper'

describe Importer do
  describe "#process_markdown" do
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
end
