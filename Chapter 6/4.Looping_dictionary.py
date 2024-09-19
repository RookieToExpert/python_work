#Looping through all key-value pairs
#6.1:Person
person = {
    'first_name' : 'ray',
    'last_name' : 'tang',
    'age' : 22,
    'city' : 'shanghai'
}
# print(person.items())
# print(person)

#Print all keys and corresponding values in a dictionary
for key, value in person.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

#another example
favorite_languages = {
    'jenny': 'python',
    'ray': 'python',
    'vergo': 'java',
    'eva': 'c++'
}

for name, language in favorite_languages.items():
    print(f"\n{name.title()}'s favorite coding language is {language.title()}")
