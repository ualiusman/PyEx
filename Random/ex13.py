#Exercise 13:
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

def printFibonacciNumbers(n):
    f1 = 0
    f2 = 1
    if( n < 1):
        return
    for s in range(0,n):
        s = s
        print(f2, end =" ")
        next  = f1 + f2
        f1 = f2
        f2 = next

num  = validation_input()
printFibonacciNumbers(num)