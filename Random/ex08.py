#Exercise 08:
import random

def choice(c):
    print(c)

def validation_input():
    while True:
        try:
            user_input = int(input("tell me your choice:"))
            if user_input not in range(1,4):
                print("enter only 1 to 3 number")
                continue
            if type(user_input) == int:
                break
        except ValueError:
            print("enter a valid number")
            continue
    return user_input

def print_score(h_score, c_score):
    print("Score:""\nPlayer:",h_score,"\nComputer:",c_score)


def result(h_choice, c_choice):
    game_result = (3 + h_choice - c_choice) % 3
    user_score = (0.5,1.0, 0.0)[game_result]
    return (user_score, 1.0 -  user_score)

print('''1 - Rock
2 - Paper
3 - Scissors''')
human_score = 0
computer_score = 0
while True:
    user = validation_input()
    ai = random.randint(1,3)
    choice(ai)
    human_score,computer_score = result(user,ai)
    print_score(human_score,computer_score)
    command = int(input("enter 0 to quit:"))
    if command ==0:
        break


