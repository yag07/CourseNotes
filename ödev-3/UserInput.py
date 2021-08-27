t = 0

while True:
    b= input("Toplamak istediğiniz sayıyı giriniz: ")
    if (b == "q" or b == "Q"):
        break
    a= int(b)
    t = t + a
    print("Toplam: ",t) 
