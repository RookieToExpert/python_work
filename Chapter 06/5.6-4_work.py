#6.4 Glossary 2 
person = {
    'first_name' : 'ray',
    'last_name' : 'tang',
    'age' : 22,
    'city' : 'shanghai'
}

for key, value in person.items():
    print(f"The key is: {key} and the value is: {value}")

#6.5 Rivers
rivers = {
    'shanghai' : 'huangpu',
    'sichuan' : 'dujiangyan',
    'heilongjiang' : 'huanghe',
    'beijing' : 'he'
}
#Run a for loop to print both city and river
for city, river in rivers.items():
    print(f"The {river} runs through {city}")
#Print all the rivers
print("Here are the rivers in the list:")
for river in rivers.values():
    print(f"The river is: {river}")
#Print all the cities
print("Here are the cities in the list:")
for city in rivers.keys():
    print(f"The citiy is: {city}")


#6.6. Polling
favorite_languages = {
    'jenny': 'python',
    'ray': 'python',
    'vergo': 'java',
    'eva': 'c++'
}

peoples = ['ray', 'thomas', 'jenny', 'chris']

#Loop throughthe people who should take the poll
for people in peoples:
    if people not in favorite_languages.keys():
        print(f"Let's take the pool {people.title()}, tell me your favorite language!")
    else:
        print(f"{people.title()}, you have already took the pool, your favorite language is {favorite_languages[people]}")

