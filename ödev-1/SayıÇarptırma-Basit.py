# -*- coding: utf-8 -*-
"""
Created on Mon May 17 22:38:08 2021

@author: YAG

"""
liste=[]

x=1

while len(liste)<3:
    sayı=int(input("{}. sayıyı giriniz:".format(x)))
    liste.append(sayı)
    x +=1
    
print(liste)
    
sonuc= liste[0]*liste[1]*liste[2]

print(sonuc)