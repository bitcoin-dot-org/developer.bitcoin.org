require_relative 'spec_helper'

describe TableFixer do
  describe "#fixup_tables" do
    it "pads rows with spaces which are not aligned" do
      rst = <<EOT
+----+----+
| a  | b |
+====+====+
| c | d  |
+----+----+

+----+-----+--+
| aa | bb |  |
+====+=====+==+
| cc | dd  |  |
+----+-----+--+

+---+---+
| aa | b |
+===+===+
| c | dd |
+---+---+
EOT

            expected = <<EOT
+----+----+
| a  | b  |
+====+====+
| c  | d  |
+----+----+

+----+-----+--+
| aa | bb  |  |
+====+=====+==+
| cc | dd  |  |
+----+-----+--+

+----+----+
| aa | b  |
+====+====+
| c  | dd |
+----+----+
EOT
      expect(subject.fixup_tables(rst)).to eq(expected)
    end
  end

  describe "#calculate_column_widths" do
    context "without given column widths" do
      it "calculates thin lines" do
        expect(subject.calculate_column_widths("+---+-+--+")).to eq([3, 1, 2])
      end

      it "calculates thick lines" do
        expect(subject.calculate_column_widths("+===+=+==+")).to eq([3, 1, 2])
      end

      it "calculates cells" do
        expect(subject.calculate_column_widths("| c | | x|")).to eq([3, 1, 2])
      end

      it "calculates cells with plus as content" do
        expect(subject.calculate_column_widths("| c+ | | x|")).to eq([4, 1, 2])
      end
    end

    context "with given column widths" do
      it "maximizes widths" do
        expect(subject.calculate_column_widths("+----+-+--+", [2, 1, 3])).to eq([4, 1, 3])
      end
    end
  end

  describe "#fixup_line" do
    it "fixes cells" do
      expect(subject.fixup_line("| a | b c |", [4, 7])).to eq("| a  | b c   |")
    end

    it "fixes cells with plus sign" do
      expect(subject.fixup_line("| a+ | b c |", [4, 7])).to eq("| a+ | b c   |")
    end

    it "fixes thick lines" do
      expect(subject.fixup_line("+==+=+", [3,1])).to eq("+===+=+")
    end

    it "fixes thin lines" do
      expect(subject.fixup_line("+--+-+", [3,1])).to eq("+---+-+")
    end
  end
end
