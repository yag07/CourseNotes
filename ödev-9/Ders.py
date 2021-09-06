def triple(c):
    return c * 3

print(map(triple,range(10)))

print(list(map(triple,range(10))))

print(list(map(lambda x : x ** 2, range(10))))

l = list(range(10))
l2 = list(range(11,20))
l3 = list(range(21,31))

print(list(map(lambda x,y,z : (((x*y)/(z))) , l , l2, l3)))

from functools import reduce

def fak(x,y):
    return x * y

print(reduce(fak,range(1,6)))


def top(x,y):
    return x + y

print(reduce(top,range(1,6)))


def triplet(x):
    if (x % 3 == 0):
        return True

print(list(filter(triplet,range(50))))


i = 0

liste = list()

while (i < len(l) and i < len(l2)):

    liste.append((l[i],l2[i]))
    i += 1

print(liste)

print(list(zip(l,l2)))

for k ,  l in zip(l,l2):
    print(k,l)

liste2 = list()

while (i < len(liste)):

    liste2.append((i,l[i]))
    i += 1

print(liste2)

print(list(enumerate(liste)))


for i ,j in enumerate(liste):
    if (i % 2 == 0 ):
        print(j)

"""
def pozitif(x):
    if (not i):
        return False
    return True

def negatif(y):
    if i:
        return True
    return False

"""



x =range(5)

print(list(x), all(x) , any(x))






















