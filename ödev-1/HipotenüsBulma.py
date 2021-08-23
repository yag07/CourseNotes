# -*- coding: utf-8 -*-
"""
Created on Tue May 18 00:01:59 2021

@author: YAG
"""

liste=[]

x=1

while len(liste)<2:
    sayı=float(input("{}. kenarı giriniz:".format(x)))
    liste.append(sayı)
    x +=1
    
print(liste)

h= ((((liste[0])**2)+((liste[1])**2))**0.5)

print(h)