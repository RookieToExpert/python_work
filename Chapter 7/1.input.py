#An example of input
message = input("Tell me somthing, and I will repeat it back to you: ")
print(message)


#Another example
name = input("Please enter your name: ")
print(f"\nHello, {name}!")


#Use += sign
prompt = "If you share your name, we can personalize the messages you see. \nWhat is your first name? "
# prompt += "\nWhat is your first name?"
# 

name = input(prompt)
print(f"\nHellow, {name}!")

#If the input is a number, use int()
age = input("How old are you? ")
age = int(age)

if age >= 18:
    print("\nYou are an adult now")
else:
    print("You are still a kid!")