"""
10-6 Addition
One common problem when prompting for numerical input 
occurs when people provide text instead of numbers. When you try to convert 
the input to an int, you’ll get a ValueError. Write a program that prompts for 
two numbers. Add them together and print the result. Catch the ValueError if 
either input value is not a number, and print a friendly error message. Test your 
program by entering two numbers and then by entering some text instead of a 
number
"""
def addition_two_numbers():
    print("Give me two numbers, and I'll divide them.")
    print("Enter 'q' to quit.")
    a = input("\nFirst number: ")
    if a =='q':
        return
    b = input("Second number: ")
    if b == 'q':
        return
    try:
        answer = int(a) / int(b)
        print(answer)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    except ValueError:
        print('Please enter a integer!')
       

addition_two_numbers()