liste = []
m1 = [[0 for x in range(11)] for y in range(11)] # matriks oluşturmak için
#print(m1)

for i in range (11):
    for j in range (11):
        # print("{} x {} = {} ".format(i,j,i*j))
        a = i*j
        liste.append(a)
        m1[i][j] = a

# print(liste)
[print(*line) for line in m1] #matriksi tablo şeklinde göstermek için

