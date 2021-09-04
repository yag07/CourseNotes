d3_liste = list()
d4_liste = list()
d5_liste = list()
d6_liste = list()

def hesap(satır):

    satır = satır[:-1]
    #print(satır)

    liste = satır.split(",")
    #print(liste)

    d1 = float(liste[1])

    d2 = float(liste[2])

    d3 = float(liste[3])

    d4 = float(liste[4])

    d5 = float(liste[5])

    d6 = float(liste[6])

    if (d1 > 0 or d2 > 0):
        d3_liste.append(d3)
        d4_liste.append(d4)
        d5_liste.append(d5)
        d6_liste.append(d6)

    #rint(len(d6_liste))


with open("sample.csv","r") as csv_file:
    for i in csv_file:
        hesap(i)

    d3min = min(d3_liste)
    d3max = max(d3_liste)
    d3avg = sum(d3_liste)/(len(d3_liste)+1)

    print(f"D3 listesi: min {d3min} , max {d3max} , avg {d3avg:.3f} ")

    d4min = min(d4_liste)
    d4max = max(d4_liste)
    d4avg = sum(d4_liste)/(len(d4_liste)+1)

    print(f"D4 listesi: min {d4min} , max {d4max} , avg {d4avg:.3f} ")

    d5min = min(d5_liste)
    d5max = max(d5_liste)
    d5avg = sum(d5_liste)/(len(d5_liste)+1)

    print(f"D5 listesi: min {d5min} , max {d5max} , avg {d5avg:.3f} ")

    d6min = min(d6_liste)
    d6max = max(d6_liste)
    d6avg = sum(d6_liste)/(len(d6_liste)+1)

    print(f"D6 listesi: min {d6min} , max {d6max} , avg {d6avg:.3f} ")

    with open("sonuc.txt" , "w" , encoding = "utf-8") as file:
        file.write(str(d3_liste))
        file.write(str(d4_liste))
        file.write(str(d5_liste))
        file.write(str(d6_liste))