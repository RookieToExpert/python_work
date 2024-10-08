#Inheritance a child class from its parent class
#Parent class from four
class Restaurant:
    """Create Restaurant with name and cusine"""

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type
        self.number_served = 0
        self.customer_numbers = 0
    
    def describe_resturant(self):
        print(f"This is my restaurant, its name is {self.name}.")
        print(f"And my resturant serve {self.cuisine} type of food.")

    def open_restaurant(self):
        print(f"My restaurant {self.name} that serve {self.cuisine} type of food, will open tomorrow!")

    #Add a method called set_number_served()
    def set_number_served(self, served_number):
        """Manually set the served dishes number"""
        if served_number >= self.number_served:
            self.number_served = served_number
            print(f"The current number of dishes severd is {self.number_served}.")
        else:
            print(f"Please enter a number greater than current value {self.number_served}.")

    #Add a method called increment_number_served()
    def increment_number_served(self, increment_dish):
        """Add the enter value of dishes to the current dishes value."""
        if increment_dish >= 0:
            self.number_served += increment_dish
            print(f"The current number of dishes severd is {self.number_served}.")
        else:
            print("Please enter a number greater than 0!!")
    
    #Add a method called customer_number()
    def customer_number(self):
        """Add current customer number by 1."""
        self.customer_numbers += 1
        print(f"The current customer's number is {self.customer_numbers}.")
    
    #Add a method called reset_customer_number()
    def rest_customer_number(self):
        """Reset the customer number to 0."""
        self.customer_numbers = 0
        print(f"The current customer's number has been reset to {self.customer_numbers}.")

#Child class
#Defining attributes and methods for the cild class
class RayRestaurant(Restaurant):
    """Represent aspects of restaurant, spcific to ray's resaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialized attributes of the parent class"""
        super().__init__(restaurant_name, cuisine_type)
        self.ray_money = 1_000

    def print_current_money(self):
        """Print all the money ray has."""
        print(f"Your current money is {self.ray_money}.")
    
    def describe_resturant(self):
        """Overrite this method"""
        print("This is Ray's motherfucker restaurant.")
    
ray_restaurant1 = RayRestaurant("ray_restaurant1", "GuangDong")
print(ray_restaurant1.customer_numbers)
ray_restaurant1.print_current_money()
ray_restaurant1.describe_resturant()

#Composition
class DadRestaurant(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        """Ray's dad restaurant"""
        super().__init__(restaurant_name, cuisine_type)
        self.son = RayRestaurant("ray", "guangdong")

dadrestaurant = DadRestaurant("dadrestaurant", 'chengdu')
dadrestaurant.son.print_current_money()
dadrestaurant.describe_resturant()
dadrestaurant.son.describe_resturant()

