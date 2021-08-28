d = { 0 : "Sıfır", 1 : "Bir" , 2 : "İki" , 3 : "Üç" , 4 : "Dört" , 5 : "Beş" , 6 : "Altı" , 7 : "Yedi" , 8 : "Sekiz" , 9 : "Dokuz" }

def o(s):

    """
    a = 0
    b = 0
    l = len(str(s))
    x = l + 1
    """
    t = [ i for i in str(s)]

    print("Sayı : {}".format(s))
    #sl = list()

    for i in t:
        i = int(i)
        print(d[i], sep='', end=' ', flush=True)
        #sl.append(d[i])
    #print(sl)
    #print(sl, end=" ")
    #print(sl, sep=' ', end='', flush=True)

    """
    while a < l :
        b = s % 10**x
        s //= 10
        x -= 1
        a += 1
        print(b, s)
    """    

sayı = int(input("Sayı giriniz: "))

o(sayı)