#Create some aliens dictionary
alien_0 = {'color': 'green', 'point' : 5}
alien_1 = {'color': 'yellow', 'point' : 10}
alien_2 = {'color': 'red', 'point' : 15}

#Put them into a list
aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

#A more realistic example
aliens = []

#Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color' : 'green', 'points' : 5, 'speed' : 'slow'}
    aliens.append(new_alien)

#Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")

#Show how many aliens have been created
print(f"Total number of alines: {len(aliens)}")

#Change the first three alien dictionary pairs
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
    print(alien)

#Put list in a dictionary
#Store information about a pizza being ordered.
pizza = {
    'crust' : 'thick',
    'toppings' : ['mushrooms', 'extra cheese'],
}

#Summarize the order.
print(f"You orderd a {pizza['crust']}-crust pizza with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")

#Double for_loop
favorite_languages = {
    'jenny': ['python'],
    'ray': ['python', 'matlab'],
    'vergo': ['python', 'java'],
    'eva': ['python', 'c']
}

# for name, languages in favorite_languages.items():
#     if len(languages) > 1:
#         print(f"\n{name.title()}'s favorite languages are:")
#         for language in languages:
#             print(f"\t{language.title()}")
#     else:
#         print(f"\n{name.title()}'s favorite languages is:")
#         for language in languages:
#             print(f"\t{language.title()}")

# Better version
for name, languages in favorite_languages.items():
    verb = "is" if len(languages) == 1 else "are"
    print(f"\n{name.title()}'s favorite languages {verb}:")
    for language in languages:
         print(f"\t{language.title()}")


#A dictionary in a Dictionary
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
 }

for username, user_infor in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_infor['first']} {user_infor['last']}"
    location =user_infor['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")