def ms(s):
    t = 0

    for i in range(1,s):
        if (s % i == 0):
            t += i
    
    return t == s

while True:
    a = abs(int(input("Başlangıç sayısını giriniz: ")))
    b = abs(int(input("Bitiş sayısını giriniz: "))) 

    for i in range(a,b+1):
        if (ms(i)):
            print("Mükemmel Sayı: ", i)
