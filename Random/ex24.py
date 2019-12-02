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


def draw_board(num):
    for n in range(num * 2 + 1):
        for i in range(num):
            if n % 2 == 0:
                print(" ---",end="")
            else:
                print("|  ",end=" ")
                if i == num-1:
                    print("|",end="")
            
            
                
        print("")
    
  
num = validation_input("Enter a Number: ")


draw_board(num)
  