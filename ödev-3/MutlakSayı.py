s = int(input("Sayıyı giriniz: "))

b = 0

for i in range(1,s):
    if(s % i == 0):
        b += i
        print("Bölenler toplamı:{} , Bölen: {}".format(b,i))
    else:
        print("{}, {}'e tam bölünmez".format(s,i))

print("{} Mükemmel Sayıdır. Bölenler toplamı {}'ya eşittir.".format(s,b))