#Passomg am Arnotrary number of arguments
#The asterisk in the parameter name *parameter name *toppings tells Python to make a tuple call toppings
def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


def make_pizza_advanced(*toppings):
    """Print the list of toppings that have been requested."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
make_pizza_advanced('pepperoni')
make_pizza_advanced('mushrooms', 'green peppers', 'extra cheese')

# Python matches positional and keyword 
# arguments first and then collects any remaining arguments in the final parameter.
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


#Using Aritrary Keyword Arguments
#The double asterisks before the parameter **user_info cause Python to create 
# a dictionary called user_info 
def build_profile(first, last, **user_info):
    """Builda dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
   

user_profile = build_profile('albert', 'einstein',
                            location='princeton',
                            field='physics')

print(user_profile['location'])



