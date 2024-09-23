# #7.8 Deli
# sandwich_orders = ['sausage', 'hambergers', 'prinkle', 'sweet']
# finished_sandwiches = []
# while sandwich_orders:
#     sandwitch = sandwich_orders.pop()
#     print(f"I made your {sandwitch} sandwitch!")
#     finished_sandwiches.append(sandwitch)

# for sandwitch in finished_sandwiches:
#     print(sandwitch)


# #7.9 No Pastrami
# sandwich_orders = ['sausage', 'hambergers', 'prinkle', 'sweet', 'sweet', 'sweet']
# print('Deli is run out of sweet.')
# while 'sweet' in sandwich_orders:
#     sandwich_orders.remove('sweet')

# print(sandwich_orders)

#7.10 Dream Vacation
poll = {}
while True:
    poll_name = input("What is your name? ")
    poll_location = input("If you could visit one place in the world,where would you go? ")
    poll[poll_name] = poll_location
    print(f"Oh, {poll_name.title()}'s favorite place is {poll_location.title()}!")
    end = input("Would you like to introduce your freind to take the poll? (yes/no) ")
    if end == 'no':
        break
   
