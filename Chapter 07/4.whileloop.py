#While loop counts from 1 to 5
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

#While and input
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. \nPlease enter the value:"

message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)