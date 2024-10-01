#9.6 Ice Cream Stand
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

class IcmCreamStand(Restaurant):
    def __init__(self, stand_name, icm_cream_type):
        """Define initial method"""
        super().__init__(stand_name, icm_cream_type)
        self.flavor = IcmCreamFlavor()



class IcmCreamFlavor:
    def __init__(self, flavor=["milk", "cocnut", "strawberry"]):
        self.flavor = flavor
        self.flavor_number = len(self.flavor)
    
    
    def print_flavor(self):
        """Print the flavor(s) of Icm Cream."""
        print("The current on-sale icm cream flavors are:")
        for single_flavor in self.flavor:
            print(single_flavor)

    def upgrade_flavor(self):
        """Increase the flavor types if too low"""
        if self.flavor_number < 5:
            print(f"The number of the Icm Cream type is {self.flavor_number}, it's lower to 5, please increase more types!")
        else:
            print("You have enough types!")
    def add_flavor(self, *flavor_type):
        """Add more flavors."""
        for flavor in flavor_type:
            self.flavor.append(flavor)
        self.flavor_number = len(self.flavor)



sunday = IcmCreamStand("Sunday", "Corn")
sunday.flavor.print_flavor()
sunday.flavor.upgrade_flavor()
sunday.flavor.add_flavor("valina", "chocolate", "blueberry")
sunday.flavor.print_flavor()
sunday.flavor.upgrade_flavor()
