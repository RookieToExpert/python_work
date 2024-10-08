#6.7 People
#Make three dictionaries of ppl
person_0 = {
    'first_name' : 'ray',
    'last_name' : 'tang',
    'age' : 22,
    'city' : 'shanghai'
}

person_1 = {
    'first_name' : 'jenny',
    'last_name' : 'ye',
    'age' : 24,
    'city' : 'shanghai'
}

person_2 = {
    'first_name' : 'vergo',
    'last_name' : 'zhang',
    'age' : 25,
    'city' : 'shanghai'
}
#Nest the dictionary into a list
#Print everything in the list that contains dictionary
people = [person_0, person_1, person_2]
for person in people:
    for key, value in person.items():
        if key == 'city':
            print(f"The city where the pEople lives is: {value}")
        else:
            print(f"The {key} of this person is: {value}")
print("-"*20, "\n")

#6.8 Pets
pet_0 = {
    'name' : 'fantuan',
    'owner' : 'michael'
}

pet_1 = {
    'name' : 'anbei',
    'owner' : 'niang'
}

pet_2 = {
    'name' : 'daidai',
    'owner' : 'ray'
}

pet_list = [pet_0, pet_1, pet_2]

for pet in pet_list:
    for name in pet.values():
        print(f"The pet's name is {name}, and its owner is {name.title()}")
print("-"*20, "\n")


#6.9 Favorite places
favorite_places = {
    "ray" : ['virginia', 'chengdu', 'shanghai'],
    "jenny" : ['shanghai', 'beijing'],
    "vergo" : ['henan', 'weichuang']
}


for name, places in favorite_places.items():
    print(f"What is your favorite place, {name}?")
    print(f"{name}: My favorite palce is: ")
    for place in places:
        print(place.title())
print("-"*20, "\n")


#6.10 Favorite numbers
favorite_number = {
    'ray' : [22, 33, 44],
    'jenny' : [3, 55, 1],
    'vergo' : [5, 11, 44],
    'mike' : [6, 231, 78]
}

for name, numbers in favorite_number.items():
    print(f"{name.title()}'s favorite number is: {numbers}")
print("-"*20, "\n")


#6.11 Cities
cities = {
    'shanghai' : {
        'country' : 'China',
        'population' : 16_000_000,
        'fact' : 'good'
    },
    'blacksburg' : {
        'country' : 'America',
        'population' : 1_3000_000,
        'fact' : 'decent' 
    },
    'mubapei' : {
        'country' : 'cc',
        'population' : 1_000,
        'fact' : 'poor'
    }
}

for city, infor in cities.items():
    print(f"The description of the {city.title()} is as below:",
          f"\nCountry: infor['country']", 
          f"\nPopulation: infor['population']",
          f"\nFact: infor['fact']")
print("-"*20, "\n")


