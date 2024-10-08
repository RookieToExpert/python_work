from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()
contents = contents.strip()
print(contents)

lines = contents.splitlines()
for line in lines:
    print(line)

#Working with a File's Contents
pi_string = ''
for line in lines:
    pi_string += line.strip()


print(pi_string)
print(len(pi_string))
# Only print the first 7 digits
print(pi_string[:9])

# Check if your birthday contained in Pi
path = Path('pi_dec_1m.txt')
birthday = '8222022'

pi_string = path.read_text()
complete = ''
lines = pi_string.splitlines()
for line in lines:
    complete += line.strip()
print(len(complete))
if str(birthday) in complete:
    print('Your birthday is in Pi!')
else:
    print('Your birthday is not in pi!')
