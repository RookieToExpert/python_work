toppings = ['mushrooms', 'fries', 'cheese']

# for topping in toppings:
#     if topping == 'peppers':
#         print(f"Sorry, we run out of {toppings[1]} now!")
#     else:
#         print(f"Adding {topping}!!")

# toppings = []

#Checking if a list is not empty
# if toppings:
#     for topping in toppings:
#         print(f"Adding {topping}!!")
#     print("\nFinished making the pizza!!")
# else:
#     print("Are you sure you want a plain pizza?")

#Checking if items in list A are in list B 
availale_toppings = ['mushrooms', 'peppers', 'cheese', 'pepperoni', 'pineapple', 'olivees']
#Multiple lists
for topping in toppings:
    if topping in availale_toppings:
        print(f"Adding {topping}")
    else:
        print(f"{topping} is currently not available!")

print("\nFinshed making your pizza!")