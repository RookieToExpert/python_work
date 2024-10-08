# Learning Python
from pathlib import Path as pa
path = pa('summary.txt')
whole_content = path.read_text()
print(whole_content)

one_line = ''
for line in whole_content.splitlines():
    one_line += line.lstrip()
print(one_line)

# replacing python with C
new_line = one_line.replace('python', 'C')
print(new_line)