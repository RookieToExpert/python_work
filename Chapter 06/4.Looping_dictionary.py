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


#Looping only key in a dictionary
#Looping through the keys is actually the default behavior when looping 
#through a dictionary
#But putting a keys() method can make your code more readable
for name in favorite_languages.keys():
    print(f"Introducing {name.upper()} to you!")

#If and for loop work together with dicitionary
name_list = ['ray', 'michael', 'jenny', 'ben']
for name in favorite_languages.keys():
    print(f"Hi, {name.title()}, good to see you!")

    if name in name_list:
        print(f"Hi {name.title()}, I know your favorite language is {favorite_languages[name]} ")

#Another example
name_list = ['ray', 'michael', 'jenny', 'ben']
for name in name_list:
    print(f"Hi, {name.title()}, good to see you!")

    if name in favorite_languages.keys():
        print(f"Hi {name.title()}, I know your favorite language is {favorite_languages[name]} ")


#Looping through a dictionary's keys in a particular order
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")


#Looping through all values in a dictionary
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

#Use set to reduce the duplication,  a set is a collection in which each item must be unique/
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

#You can build a set directly using brases and separating the elements with commas
set = {
    'repeated',
    'repeated',
    'Unique',
    'Unique2'
}
print(set)