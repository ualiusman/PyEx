#Exercise 05:
import random 

a = [random.randrange(1, 100, 1) for i in range(100)]
b = [random.randrange(1, 100, 1) for i in range(100)]
c = []
for n in a:
    if n in b:
        c.append(n)

c  = list(dict.fromkeys(c))

for n in c:
    print(n)

        


