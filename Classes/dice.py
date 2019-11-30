from random import randint

class Dice():
    def __init__(self,sides = 6):
        self.sides = sides
    
    def roll_die(self):
        return randint(1,self.sides)


if __name__ == "__main__":
    d = Dice()
    print(d.roll_die())
    d10 = Dice(10)
    d20 = Dice(20)
    
    print(d10.roll_die())
    print(d20.roll_die())