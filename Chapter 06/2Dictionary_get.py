#Create a dictionary with one kind of information
favorite_languages = {
    'jenny': 'python',
    'ray': 'python',
    'vergo': 'java',
    'eva': 'c++'
}

language = favorite_languages['jenny'].title()
print(f"Jenny's favorite language is {language}.")

#Get method to set a default value that will be returned if the key doesn't exist
#The first one will give an error if no vicky exists
#When use get method, it can throw a message instead an error
#print(favorite_languages['vicky'])
print(favorite_languages.get('vicky', 'No such user'))
