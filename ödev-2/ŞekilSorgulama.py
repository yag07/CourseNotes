# -*- coding: utf-8 -*-
"""
Created on Fri May 21 22:56:35 2021

@author: YAG
"""

geo=int(input("Üçgen için 3, dört kenarlı şekil için 4 yazın"))

if geo == 4:
    liste=[]
    x=1

    while len(liste)<4:
        s=float(input("{}. kenarı giriniz".format(x)))
        liste.append(s)
        x +=1
        liste.sort(reverse=True)
    
    print(liste)
    
    mean= sum(liste) / len(liste)
    dd= sum(liste) - (liste[0] + liste[1])
    cc= liste[2] + liste[3]
        
    if mean == liste[0]:
        print("Kare")
    elif dd == cc and liste[0] == liste[1] and liste[2] == liste[3]:
        print("Dikdörtgen")
    else:
        print("Dörtgen")
    
elif geo == 3:
    liste2=[]
    y=1

    while len(liste2)<3:
        d=float(input("{}. kenarı giriniz".format(y)))
        liste2.append(d)
        y +=1
        liste2.sort(reverse=True)
    
    mean2= sum(liste2) / len(liste2)
    dk= liste2[0] + liste2[1]
    db= liste2[1] + liste2[2] 

    if mean2 == liste2[0]:
        print("Eşkenar Üçgen")
    elif dk == 2 * liste2[0]: 
        print("İkizkenar üçgen, atmış dereceden küçük")
    elif db == 2 * liste2[2]:
        print("İkizkenar üçgen, atmış dereceden büyük")
    elif mean2 > liste2[2]:
        print("Çeşitkenar üçgen")
    elif mean2 < liste2[2]:
        print("Üçgen belirtmiyor")
    else:
        print("Bu sefer olmadı")
else:
    print(" 3 veya 4 yazmalısınız")