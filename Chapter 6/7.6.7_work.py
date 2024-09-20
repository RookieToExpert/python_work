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

people = [person_0, person_1, person_2]
for person in people:
    for key, value in person.items():
        if key == 'city':
            print(f"The city where the pEople lives is: {value}")
        else:
            print(f"The {key} of this person is: {value}")
print("......")