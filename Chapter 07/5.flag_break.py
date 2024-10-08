#While loop using flag
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. \nPlease enter the value:"
# Flag = True
# while Flag:
#     message = input(prompt)
#     if message == 'quit':
#         Flag = False
#     else:
#         print(message)

#Using break
while True:
    message = input(prompt)
    if message == 'quit':
        break
    print(message)

#Using continue
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)



    