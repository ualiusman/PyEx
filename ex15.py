#Exercise 15:


def uniqueListSet(l):
     return list(set(l))

def reveseMyString(st):
    sl = st.split()
    sl.reverse()
    return " ".join(sl)

st = input("Enter a string:")
st = reveseMyString(st)
print(st)