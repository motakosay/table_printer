#py table_code.py
text = """
Position,Text Content
Top Center,Title: "مجلة الأسرار"
Center (Below Title),Author Name & Affiliation: "محمد أحمد- كلية الأداب -قسم لغة عربية"
Center (Middle),Emblem: Circular logo of the University
Bottom Center,Publication Info: "2023"
"""


# Parse the text
lines = text.strip().split('\n')
rows = [line.split(',') for line in lines]

# Calculate column widths
col_widths = [max(len(row[i]) for row in rows) for i in range(len(rows[0]))]

# Function to format a row
def format_row(row):
    return " | ".join(cell.ljust(col_widths[i]) for i, cell in enumerate(row))

# Print the table
print(format_row(rows[0]))  # Header
print("-" * (sum(col_widths) + 3 * (len(col_widths) - 1)))  # Separator
for row in rows[1:]:
    print(format_row(row))
