#Exercise 14:


def uniqueListSet(l):
     return list(set(l))

def uniqueList(l):
    uniquelist = []
    for e in l:
        if(e not in uniquelist):
            uniquelist.append(e)
    return uniquelist

l = [1,1,2,3,4,6,6]
l = uniqueListSet(l)
l2 = uniqueList(l)
print(l)
print(l2)