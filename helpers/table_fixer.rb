class TableFixer
  def calculate_column_widths(line, column_widths = [])
    widths = []
    width = 0
    start_char = line[0]
    line.each_char do |char|
      if char == start_char
        if width > 0
          widths.append(width)
          width = 0
        end
      else
        width += 1
      end
    end

    if column_widths.empty?
      widths
    else
      if column_widths.length != widths.length
        raise "TableFixer.calculate_column_widths: arrays don't match: #{column_widths}, #{widths}"
      end
      widths.each_with_index do |value, index|
        if column_widths[index] < value
          column_widths[index] = value
        end
      end
      column_widths
    end
  end

  def fixup_line(line, column_widths)
    result = ""
    col = 0
    width = 0
    previous_char = ""
    start_char = line[0]
    line.each_char do |char|
      if char == start_char
        if width > 0
          gap = column_widths[col] - width
          if gap > 0
            result += (previous_char * gap)
          end
          width = 0
          col += 1
        end
      else
        width += 1
      end
      result += char
      previous_char = char
    end
    result
  end

  def add_table_lines(processed, table_lines, column_widths)
    table_lines.each do |table_line|
      processed << fixup_line(table_line, column_widths)
    end
  end

  # Pad table cells so that they are verticsally aligned with each other
  def fixup_tables(rst)
    processed = ""
    table_lines = []
    column_widths = []
    rst.each_line do |line|
      if table_lines.empty? && line.start_with?("+")
        column_widths = calculate_column_widths(line)
        table_lines.append(line)
      elsif !table_lines.empty? && !line.start_with?("|", "+")
        add_table_lines(processed, table_lines, column_widths)
        table_lines = []
      elsif !table_lines.empty?
        column_widths = calculate_column_widths(line, column_widths)
        table_lines.append(line)
      end

      if table_lines.empty?
        processed += line
      end
    end
    if !table_lines.empty?
      add_table_lines(processed, table_lines, column_widths)
    end
    processed
  end
end
