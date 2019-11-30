class Resturant():
    def __init__(self,restaurant_name, cusine_type):
        self.restaurant_name = restaurant_name
        self.cusine_type = cusine_type
        self.number_served = 0
    
    def set_number_served(self, number_served):
        self.number_served = number_served
    
    def increment_number_served(self):
        self.number_served += 1
    
    
    def describe_restaurant(self):
        print("This is " + self.restaurant_name.title() + " of type " + self.cusine_type.title() + " with " + str(self.number_served) +" people served")
    
    
    def open_restaurant(self):       
        print("restaurant is open")
        




 