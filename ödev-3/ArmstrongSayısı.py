l = input("Sayıyı giriniz: ")

s= int(l) #str^den int e çevirdik

k = len(l) # int değerinin uzunluğu olmadığı için ayrı ayrı aldık

b = 0

t = 0

tn = s 

x = 1

while ( 0 < tn):
    print(x,". bölme işlemi")

    b = tn % 10 #10'a bölünme sayısı, üstünü alacağımız saayıları bulmak için
    print("10'a bölünme sayısı.", b)

    t += b**k
    print("{} üstü {} : {} , Toplam: {} ".format(b,k, b**k,t))

    tn //= 10 #bölme işleminin sonucunu bir alt tam sayıya yuvarlar
    print("Diğer ondalıkları bulmak için oluşturulan sayı: ", tn)

    x += 1

if (t == s):
    print(s," Bir Armstrong Sayısıdır.")
else:
    print(s," Bir Armstrong Sayısı değildir.")