#8.3 T-Shirt
# def make_shirt(size, message):
#     print(f"The size your choose for the shirt is {size}, and {message} is on it.")

# make_shirt('large', 'Make American great again!')
# make_shirt(message = 'Make China Great Again!', size = 'small')

#8.4 Large Shirts
def make_shirt(message = 'I love Python', size = 'large'):
    print(f"The size your choose for the shirt is {size}, and {message} is on it.")

make_shirt()
make_shirt('I hate Python', 'small')
make_shirt(size = 'medium', message = 'I kinda like Python')

#8.5 Cities
def describe_city(city, country = 'China'):
    print(f"The {city.title()} is in {country.title()}")

describe_city('ShangHai')
describe_city('Toyko', 'Japan')
describe_city(city = 'Blacksburg', country = 'America')