# #7.4 Pizza Toppings
# prompt = "\nTell me what pizza topping you would like to order:"
# prompt += "\nEnter 'quit' to end the program. \nPlease enter here: "
# while True:
#     message = input(prompt)
#     if message == 'quit':
#         print("Thanks for coming to the store!")
#         break
#     print(f"I will add {message} on your pizza!")

#7.5 Movie tickets
prompt = "\nTell me your age:"
prompt += "\nEnter 'quit' to end the program. \nPlease enter here: "
while True:
    age = int(input(prompt))
    if age < 3:
        print("It's free for you!")
    elif 3 <= age <=12:
        print("You need to pay 10 bucks for your ticket.")
    else:
        print("You need to pay 15 bucks for your ticket.")
    break