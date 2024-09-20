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