# 9.1 Make a class called Restaurant
# Set a default value as profit
class Restaurant:
    """Create Restaurant with name and cusine"""

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type
        self.profit = 0
    
    def describe_resturant(self):
        print(f"This is my restaurant, its name is {self.name}.")
        print(f"And my resturant serve {self.cuisine} type of food.")

    def open_restaurant(self):
        print(f"My restaurant {self.name} that serve {self.cuisine} type of food, will open tomorrow!")

    def profit_count(self):
        """Print a profit of the restaurant."""
        print(f"This restaurant has {self.profit} bucket of profit.")

my_restaurant = Restaurant("Jenny's restaurant", 'ShangHai')

my_restaurant.profit_count()

# Modify the parameter
my_restaurant.profit = 10_00
my_restaurant.profit_count()


