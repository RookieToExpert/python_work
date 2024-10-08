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


#Modify value
ray_restaurant = Restaurant("ray's restaurant", "ChengDu")
print(f"{ray_restaurant.name} has serverd {ray_restaurant.number_served} dish(es).")
ray_restaurant.set_number_served(510)
ray_restaurant.set_number_served(499)
ray_restaurant.increment_number_served(20)
ray_restaurant.increment_number_served(-231)
ray_restaurant.customer_number()
ray_restaurant.customer_number()
ray_restaurant.customer_number()
ray_restaurant.customer_number()
ray_restaurant.rest_customer_number()
