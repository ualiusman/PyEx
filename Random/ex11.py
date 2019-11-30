#Exercise 11:
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

def isPrime(num):
    factors =[]
    if num ==0:
        return False
    for x in range(1,num+1):
        if num % x == 0:
            factors.append(num/x)
    if len(factors) > 2:
        return False
    else:
        return True

number = validation_input()
result = isPrime(number)
if result == True:
    print("number is prime")
else:
    print("number is not prime")

        


