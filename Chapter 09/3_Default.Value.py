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
    
    #Modify the default value through a method
    def update_profit(self, profit):
        """
        Modify the profit to the given value.
        Reject the change if iy attemps to roll the profit back.
        """
        if profit >= self.profit:
            self.profit = profit
        else:
            print("You can't enter a number lower than the current profit.")
    
    #Incrementing an value
    def increment_profit(self, profits):
        """Add the given amount to the profit."""
        if profits >= 0:
            self.profit += profits
        else:
            print("Please enter a postiive number greater than 0.")
my_restaurant = Restaurant("Jenny's restaurant", 'ShangHai')

my_restaurant.profit_count()

# Modify the parameter
my_restaurant.profit = 10_00
my_restaurant.profit_count()
my_restaurant.update_profit(5_0000000_0)
my_restaurant.profit_count()
my_restaurant.update_profit(1_000)
my_restaurant.increment_profit(50)
my_restaurant.profit_count()
my_restaurant.increment_profit(-33)


