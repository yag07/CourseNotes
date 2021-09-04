file = open("Deneme.txt","a",encoding="utf-8")  # a yerine w kullanırsan içeriği sıfırlayarak dosya oluşturuyor(varsa önceki halini siliyor)

file.write("Merhaba Dünya\n") #

file.close() #kapatmazsak büyük dosyalar bilgisayarı yavaşlatabilir


file = open("Deneme.txt","r",encoding="utf-8") #okunabilir olarak dosya açma , utf-8 Türkçe ile uyumlu olması için

for i in file:
    print(i, end="")

file.close()


file = open("Deneme.txt","r",encoding="utf-8") 

liste = file.readlines()

print(liste)

file.close()


file = open("Deneme.txt","r",encoding="utf-8") 

ic = file.read() #readline tek tek sırayla satırları okuyor, her defasında bir satır atlıyor, read() ise tümünü okuduktan sonra en sonda duruyor

print("İçerik: ",ic)

file.close()


"""

file = open("Deneme.txt","w",encoding="utf-8")

file.close()

"""

file = open("C:/Users/YAG/OneDrive/Masaüstü/Deneme2.txt", "w" ,encoding="utf-8")

file.close()

with open("Deneme.txt" , "r" , encoding = "utf-8") as file:
    for i in file:
        print(i, end="")

with open("Deneme.txt" , "r" , encoding = "utf-8") as file:
    file.seek(5) #imleci hareket ettirmeye yarıyor
    icerik = file.read(20)
    print(icerik)
    print("İmleç {}. baytta : ".format(file.tell()))

with open("Deneme.txt" , "r+" , encoding = "utf-8") as file: #hem read hem write
    file.seek(15) #imleci hareket ettirmeye yarıyor
    file.write("Deneme")
    print(file.read())

with open("Deneme.txt" , "a" , encoding = "utf-8") as file:  #dosyanın sonuna ekleme için a metoduyla açıyoruz
    file.write("Deneme bir iki...\n")
 
with open("Deneme.txt" , "r+" , encoding = "utf-8") as file: #dosyanın başına ekleme
    index = file.read()
    index = "İlk satır\n" + index
    file.seek(0)
    file.write(index)
    print(index)

with open("Deneme.txt" , "r+" , encoding = "utf-8") as file: #dosyanın herhangi bir yerine ekleme, ben tam ortayı seçtim
    liste = file.readlines()
    a = len(liste) // 2
    liste.insert(a,"Little little in the middle\n")
    file.seek(0)
    for i in liste:  #yerine file.writelines(liste) de kullanabilirdik
        file.write(i)
    print(file.read())