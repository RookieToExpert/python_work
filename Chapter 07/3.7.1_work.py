# #7.1 Rental Car
# car = input("What kind of rental car do you like? ")
# print(f"\nLet me see if I can find you a {car}.")

# #7.2 Restaurant Seating
# people = input("How many people are in your dinner group? ")
# people = int(people)

# if people > 8:
#     print(f"Since you have more than {people} people, you'll have to wait for a table.")
# else:
#     print("The table is ready for you guys!")


#7.3 Multiples of Ten
prompt = ("Please enter a number,")
prompt += ("I will let you know if it's a multiple number of 10 or not: " )
number = int(input(prompt))
if number % 10 == 0:
    print(f"Yes, the number {number} is a mutiple of 10.")
else:
    print(f"No, this number {number} is not a mutiple of 10!")