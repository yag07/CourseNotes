# -*- coding: utf-8 -*-
"""
Created on Fri May 21 22:44:48 2021

@author: YAG
"""
liste=[]
x=1

while len(liste)<2:
    s=float(input("{}. vize notunu giriniz".format(x)))
    liste.append(s)
    x +=1
    
else:
    s=float(input("Final notunu giriniz"))
    liste.append(s)
    n=liste[0]*0.3 + liste[1]*0.3 + liste[2]*0.4
    print("ortalama",n)
    if n>90:
        print("AA")
    elif 70<n<90:
        print("B")
    elif 50<n<70:
        print("C")
    else:
        print("Kaldı")