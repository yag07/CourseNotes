# -*- coding: utf-8 -*-
"""
Created on Mon May 17 22:51:05 2021

@author: YAG
"""

liste=[]

i=0
j=input("Çarpmak istediğiniz sayı adedini giriniz:")
k=int(j)
x=1
     
while i<k:
    sayı=int(input("{}. sayıyı giriniz:".format(x)))
    liste.append(sayı)
    x +=1
    i +=1
else:
    print(liste)

def carp(liste): 
    c=1
    for a in liste:
        c=c*a
        print(c)
    return c 

print(carp(liste))

