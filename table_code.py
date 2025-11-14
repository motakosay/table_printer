# table_code.py
import sys

# make sure pass file name
if len(sys.argv) < 2:
    print("Usage: python table_code.py <input.txt>")
    sys.exit(1)

filename = sys.argv[1]

# read .txt file
with open(filename, "r", encoding="utf-8") as f:
    text = f.read()

lines = [line for line in text.strip().split('\n') if line.strip()]  # تجاهل الأسطر الفارغة
rows = [line.split(',') for line in lines]

num_cols = len(rows[0])

# ضمان أن كل صف له نفس عدد الأعمدة
rows = [row if len(row) == num_cols else row + [""] * (num_cols - len(row)) for row in rows]

col_widths = [max(len(row[i]) for row in rows) for i in range(num_cols)]

def format_row(row):
    return " | ".join(row[i].ljust(col_widths[i]) for i in range(num_cols))

print(format_row(rows[0]))
print("-" * (sum(col_widths) + 3 * (num_cols - 1)))  # فاصل
for row in rows[1:]:
    print(format_row(row))
