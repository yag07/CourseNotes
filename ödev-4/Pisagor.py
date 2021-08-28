def pis():
    liste = list()

    for i in range(1,101):
        for j in range(1,101):
            h = ( ( (i**2) + (j**2) ) ** ( 0.5 ) )
            if (h == int(h)):
                liste.append((i,j,int(h)))
                #print(h)
    #print(liste)
    return liste

for i in pis():
    print(i)