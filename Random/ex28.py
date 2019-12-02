#Exercise 28:



def validation_input(help_text="Enter a number:"):
    while True:
        try:
            user_input = int(input(help_text))
            if type(user_input) == int:
                break
        except ValueError:
            print("enter a valid number")
            continue
    return user_input


def max3(a,b,c):
    if b > a: a = b
    if c > a: a = c
    return a
  
first = validation_input("Enter first Number: ")
second = validation_input("Enter second Number: ")
third = validation_input("Enter third Number: ")

m  = max3(first,second,third)
print(m)
  