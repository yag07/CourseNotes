from functools import reduce

karem = [(3,4) , (10,3) , (5,6) , (1,9)]
ucgenim = [(3,4,5),(6,8,10),(3,10,7),(8,15,17)]
l = list(range(2,11,2))

def kare(i):
    return i[0] * i[1]

def ucgen(i):
    if not ( (max(i) - min(i) ) == ( sum(i) - max(i) - min(i) ) ):
        return i

print(list(map(kare,karem)))

print(list(filter(ucgen,ucgenim)))


def cift(x):
    if (x % 2 == 0):
        return x

def tol(y,z):
    return y + z

liste = list(filter(cift,range(11)))

print(liste)
print(l)

for i,j in zip(karem,ucgenim):
    print(i,j)

print(reduce(lambda x,y : x + y,l)) # ya da top fonsiyonu ile
