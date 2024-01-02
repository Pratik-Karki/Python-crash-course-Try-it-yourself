class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f"The restaurant name is {self.restaurant_name}.")
        print(f"This restaurant offers {self.cuisine_type} type of cuisine.")
    def open_restaurant(self):
        print(f"The restaurant is open.")
    def set_number_served(self,number):
        self.number_served = number
    def increment_number_served(self,number):
            self.number_served += number