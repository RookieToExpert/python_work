#9.1 Make a class called Restaurant
class Restaurant:
    """Create Restaurant with name and cusine"""

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type
    
    def describe_resturant(self):
        print(f"This is my restaurant, its name is {self.name}.")
        print(f"And my resturant serve {self.cuisine} type of food.")

    def open_restaurant(self):
        print(f"My restaurant {self.name} that serve {self.cuisine} type of food, will open tomorrow!")
        

#9.2 Create an instance
my_restaurant = Restaurant('Chinese Kung Fu', 'SiChuan')

#9.3 Use Method
my_restaurant.describe_resturant()
my_restaurant.open_restaurant()

