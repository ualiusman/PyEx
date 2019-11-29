#Exercise 18:
import random
import string
def uniqueCharacters(str): 
    for i in range(len(str)): 
        for j in range(i + 1,len(str)):  
            if(str[i] == str[j]): 
                return False
    return True

def validation_input(help_text="Enter 4 digits: "):
    while True:
        try:
            user_text = input(help_text)
            if user_text == "0000":
                break;
            user_input = int(user_text)
            
            if uniqueCharacters(user_text) == False :
                 raise ValueError
            if len(user_text) != 4:
                raise ValueError
            if type(user_input) == int:
                break
        except ValueError:
            print("enter a valid input")
            continue
    return user_text



def getRandomDigits():
    return ''.join(random.sample(string.digits, 4))

def calculateBullsAndCows(digitsToGuess,digits):
    b  = 0
    c = 0
    for i in range(0,4):
        if digits[i] == digitsToGuess[i]:
            b += 1
        elif digits[i] in digitsToGuess:
            c += 1
    return b,c

def playGame():
    digitsToGuess = getRandomDigits()
    bulls  = 0
    cows = 0
    while True:
        digits = validation_input()
        bulls,cows = calculateBullsAndCows(digitsToGuess,digits)
        if bulls == 4:
            print("weldone!")
            break
        elif digits == "0000":
            break
        else:
            print(str(bulls) + " bulls", end=", ")
            print(str(cows) + " cows")
            continue
if __name__ == "__main__":
    playGame()