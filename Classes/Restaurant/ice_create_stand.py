from restuarant import Resturant
class IceCreamStand(Resturant):
    def __init__(self,restuarant_name,flavors):
        super().__init__(restuarant_name,"Cold")
        self.flavors = flavors
    
    def describe_flavors(self):
        print(self.flavors)