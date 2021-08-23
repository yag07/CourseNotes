# -*- coding: utf-8 -*-
"""
Created on Fri May 21 22:33:44 2021

@author: YAG
"""

liste=[]
x=1

while len(liste)<3:
    s=float(input("{}. sayıyı giriniz".format(x)))
    liste.append(s)
    x +=1
    liste.sort(reverse=True)

print(liste)

print("En büyük eleman: {}".format(liste[0]))

