liste = list()
fener = list()
altısaray = list()
sekiztas = list()

with open("oyuncular.txt","r" , encoding="utf-8") as file:
    for i in file:
        i = i.split(",")
        if i[1] == "Fenerbahçe\n":
            fener.append(i)
        elif i[1] == "Galatasaray\n":
            altısaray.append(i)
        elif i[1] == "Beşiktaş\n":
            sekiztas.append(i)
        else:
            print("Şampiyon olmak mümkün, Fenerbahçe olmak imkansız.")
    
    with open("fener.txt", "w",encoding="utf-8") as file2:
        file2.writelines(str(fener))

    with open("bjk.txt", "w",encoding="utf-8") as file3:
        for i in sekiztas:
            file3.writelines(i)
            
    with open("gaassaray.txt", "w",encoding="utf-8") as file4:
        for i in altısaray:
            file4.writelines(i)

    print("Fenerbahçe: \n", fener)
    print("Sekiztas: \n", sekiztas)
    print("Altısaray: \n", altısaray)  




