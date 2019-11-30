
from restuarant import Resturant
from ice_create_stand import IceCreamStand

if __name__ == "__main__":
    restaurant = Resturant("Red chilli","desi")
    restaurant2 = Resturant("Stack House","American")
    print(restaurant.restaurant_name)
    print(restaurant.cusine_type)
    restaurant.describe_restaurant()
    restaurant.open_restaurant()
    restaurant2.set_number_served(2)
    restaurant2.increment_number_served()
    restaurant2.describe_restaurant()
    
    ics = IceCreamStand("Cold bar","Red, Gree, Blud")
    ics.increment_number_served()
    ics.describe_restaurant()
    ics.describe_flavors()