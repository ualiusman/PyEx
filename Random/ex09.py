#Exercise 09:
import random

def validation_input():
    while True:
        try:
            user_input = int(input("guess a number:"))
            if type(user_input) == int:
                break
        except ValueError:
            print("enter a valid number")
            continue
    return user_input
while True:
    number = random.randint(1,9)
    i =0
    while True:
        i +=1
        num = validation_input()
        if num > number:
            print("number is high")
        elif num < number:
            print("number is low")
        else :
            print("yes number is:" + str(num))
            print("you guessed right in " + str(i) + " atempts")
            break
    command = input("type 'exit' to exits:")
    if command == 'exit':
        break


