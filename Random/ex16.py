#Exercise 16:

import random
import string

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

def randomPassword(strenth = 0,length = 10):
    if ( strenth == 0):
        letters = string.ascii_lowercase
    elif (strenth == 1):
        letters = string.ascii_letters
    elif (strenth == 2):
        letters = string.ascii_letters + string.digits
    elif (strenth == 3):
        letters = string.ascii_letters + string.digits + string.punctuation

    return ''.join(random.choice(letters) for i in range(length))



num = validation_input("Enter a string 0-3 for password strength:")
password = randomPassword(num)
print("your passowrd is: " + password)