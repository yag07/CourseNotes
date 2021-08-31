liste = {"123", "wasd" , "q456" , "78" , "werty"}

for i in liste:
    try:
        i = int(i)
        print("{} uygun.".format(i))
    except:
        print("{} uygun değil.".format(i))


def bul(sayılar):
    d = list()
    odd = list()
    for i in sayılar:
        if i % 2 == 0:
            d.append(i)
            print(d)
        else:
            odd.append(i)
            print(odd)

sayılar = range(1,10)

bul(sayılar)

while True:
    sayı = int(input("Bir sayı giriniz: "))

    if (sayı % 2 == 0):
        print("{} çift sayıdır.".format(sayı))
    else:
        raise ValueError("Sayı tek sayıdır.")
        #print("{} tek sayıdır.".format(sayı))


