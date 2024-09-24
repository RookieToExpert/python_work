#Return value in function
# def build_person(first_name, last_name):
#     """Return a dictionary of information about a person."""
#     person = {'first': first_name, 'last': last_name}
#     return person

# musician = build_person('ray', 'tang')
# print(musician)

#Another example, in the condition tests, 'None' = 'False', will not tirgger the action under the condition
def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person"""
    person = {'first' : first_name, 'last' : last_name}
    if age:
        person['age'] = age
    return person


musician = build = build_person('ray', 'tang', age=24)
print(musician)


#Using a Function with a while Loop
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    f_name = input("First name: ")
    l_name = input("Last name: ")

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")

    end_prompt = input("Do you have any other name would like to format? (yes or no?)")
    if end_prompt == 'no':
        break