"""
Exceptions
try-except block
"""
# print(5/0) # ZeroDivisionError: division by zero

# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You can't divide by zero!")


"""
Using Exceptions to prevent crashes
"""
# print("Give me two numbers, and I'll divide them.")
# print("Enter 'q' to quit.")

# while True:
#     first_number = input("\nFirst number: ")
#     if first_number =='q':
#         break
#     second_number = input("Second number: ")
#     if second_number == 'q':
#         break
#     try:
#         answer = int(first_number) / int(second_number)
#     except ZeroDivisionError:
#         print("You can't divide by 0!")
#     else:
#         print(answer)

"""
Handling the FileNotFoundError Exception
"""
from pathlib import Path as pa
# path = pa('AliceInWonderland.txt')
# try:
#     contents = path.read_text(encoding='utf-8')
# except FileNotFoundError:
#     print(f"{path} does not exist.")
# else:
#     words = contents.split()
#     num_words = len(words)
#     print(f"The file {path} has about {num_words} words.")


"""
Define a method to count words of a text file
"""
def count_words(path):
    """Count the approximate number of words in a file."""
    try:
        path = pa(path)
        words = []
        words = path.read_text(encoding='utf-8').split()
        return str(len(words))
    except FileNotFoundError:
        return None

# path = pa('AliceInWonderland.txt')
# print(f"The number of {path} is about {count_words(path)}.")

"""
Counting numbers for multiple files.
"""
filenames = ['AliceInWonderland.txt', 'guest.txt', 'nonexist.txt']
for filename in filenames:
    result = count_words(filename)
    if result == None:
        print(f"{filename} doesn't exist!")
    else:
        print(f"The number of {filename} is about {count_words(filename)}.")
    