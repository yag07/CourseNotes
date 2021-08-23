# -*- coding: utf-8 -*-
"""
Created on Mon May 17 23:56:27 2021

@author: YAG
"""

liste=[]

x=1

while len(liste)<2:
    sayı=int(input("{}. sayıyı giriniz:".format(x)))
    liste.append(sayı)
    x +=1
    
print(liste)
    
print(liste[::-1])