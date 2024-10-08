"""
10-4 Guest
Write a program that prompts the user for their name. When they 
respond, write their name to a file called guest.txt.
"""
from pathlib import Path as pa
# prompt = input('Please enter your name: ')
# path = pa(f"{prompt}_guest.txt")
# path.write_text(f"{prompt}")


"""
10-5 Guest Book
Write a while loop that prompts users for their name. Collect 
all the names that are entered, and then write these names to a file called 
guest_book.txt. Make sure each entry appears on a new line in the file.
"""
names = []
while True:
    prompt = input('Please enter your name: ')
    if prompt == 'q':
        break
    else:
        names.append(prompt)
        print(names)

print(names)

path = pa(f"guest.txt")
content = ''
for name in names:
    line = f"{name}\n"
    content += line
print(content)
path.write_text(content)