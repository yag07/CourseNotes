x = "kasjdhgaksjhgklajhgşaljqputokz.çxöcmv<işv"

freq = dict()

for val in x:
    if (val in freq):
        freq[val] += 1
    else:
        freq[val] = 1

for i,j in freq.items():
    print(f"{i} tekrar sayısı : {j}")

print(freq)

bas_harf = ""

with open("şiir.txt","r",encoding="utf-8") as file:
    for satırcık in file:
        bas_harf += satırcık[0]

print("****************************")

print(bas_harf)

print("****************************")

with open("mailler.txt","r",encoding="utf-8") as file2:
    for i in file2:
        i = i[:-1]
        if i.endswith(".com") and i.find("@") != -1:
            print(i)

print("****************************")

isim = ["Ali","Veli","Ata","Türk","Demir"]

sad  = ["Yılmaz","Öztürk","Volkan","Kaya","Beyhan"]

liste = list(zip(isim,sad))

liste.sort()

for i,j in liste:
    print(i,j)

print("****************************")

import random

for i in range(0,len(isim)):
    x = random.randrange(0,len(isim))
    y = random.randrange(0,len(sad))
    print( isim[x] , sad[y]) 
