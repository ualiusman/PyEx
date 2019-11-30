#Exercise 10:
import random 

a = random.sample(range(100), 12)
b = random.sample(range(100),10)

c = [n for n in set(a) if n in b]


for n in c:
    print(n)

        


