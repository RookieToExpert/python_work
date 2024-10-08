#8.9 Messages
messages = ['a', 'b', 'c']
def print_message(message_input):
    for message in message_input:
        print(message)

# print_message(messages)

#8.10 Sending Messages
sented_messages = []
def send_messages(message_input, sented_message_list):
    while message_input:
        sented_message = message_input.pop()
        sented_message_list.append(sented_message)

# send_messages(message_input=messages, sented_message_list=sented_messages)
# print(sented_messages, messages)


#8.11 Archived Messages
send_messages(message_input=messages[:], sented_message_list=sented_messages)
print(messages)
print(sented_messages)