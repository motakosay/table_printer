# table_code.py
import sys
import arabic_reshaper
from bidi.algorithm import get_display

# Get language from command-line argument (default = English)
if len(sys.argv) > 2:
    language = sys.argv[2].lower()
else:
    language = "en"

# Read text from .txt file (first argument)
if len(sys.argv) > 1:
    filename = sys.argv[1]
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()
else:
    print("Usage: python table_code.py <input.txt> [en|ar]")
    sys.exit(1)

# Parse the text
lines = text.strip().split('\n')
rows = [line.split(',') for line in lines]

# Calculate column widths
col_widths = [max(len(row[i]) for row in rows) for i in range(len(rows[0]))]

# Function to format a row
def format_row(row):
    formatted_cells = []
    for i, cell in enumerate(row):
        if language == "ar":
            reshaped = arabic_reshaper.reshape(cell)
            bidi_text = get_display(reshaped)
            formatted_cells.append(bidi_text.rjust(col_widths[i]))
        else:
            formatted_cells.append(cell.ljust(col_widths[i]))
    return " | ".join(formatted_cells)

# Print the table
print(format_row(rows[0]))  # Header
print("-" * (sum(col_widths) + 3 * (len(col_widths) - 1)))  # Separator
for row in rows[1:]:
    print(format_row(row))
