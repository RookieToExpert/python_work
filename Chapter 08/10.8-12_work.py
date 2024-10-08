#8-12 Sandwiches
def sandwiches_order(*ingredients):
    if len(ingredients) == 1:
        print('The ingredient you want on the sandwitch is:')
    else:
        print('The ingredients you want on the sandwitch are:')
    for ingredient in ingredients:
        print("-"*8+ingredient)

sandwiches_order('sasuage')
sandwiches_order('sasuage', 'cheese')

#8-13 User Profile
def build_profile(first, last, **user_info):
    """Builda dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
   

user_profile = build_profile('ray', 'tang', 
                             location = 'shanghai', 
                             pet = 'daidai',
                             job = 'engineer')

print(user_profile)

#8-14 Cars
def make_car(manufacturer, model_name, **overview_car):
     """Build a car infomation needs based on your input"""
     overview_car['Manufacturer'] = manufacturer.title()
     overview_car['Model_name'] = model_name.title()
     return overview_car

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)