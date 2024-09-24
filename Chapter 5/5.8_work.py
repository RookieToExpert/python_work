old_users_list = ['jenny', 'ray', 'tom', 'eric', 'fang']

#Print greeting for each user, a special greeting for ray
# for user in old_users_list:
#     if user == "ray":
#         print("Hi Ray, you the best! Have a great morning,afternoon and night!")
#     else:
#         print(f"Hi {user}, thanks for logging!")


#Make a copy of the list and deleting the old list
users_list = old_users_list[:]
del old_users_list[:]
print(old_users_list)
print(users_list)


#Checking duplicate username
new_users = ['bob', 'marry', 'tom', 'jenny', 'tony']
for user in new_users:
    if user in users_list:
        print(f"{user} is already been registered, please enter a new name.")
    else:
        print(f"You have successfully created an account with username {user}.")

print("Thanks for workig with us!")

#store the numbers 1 through 9 in a list
number_list = []
for value in range(1, 10):
    number_list.append(value)
    print(number_list)

for number in number_list:
    if number < 3 and number == 1:
        print("The ordial number of this nAumber is 1st")
    elif number == 2:
        print("The ordial number of this number is 2nd")
    elif number == 3:
        print("The ordial number of this number is 3rd")
    elif number >3:
        print(f"The ordial number of this number is {number}th")