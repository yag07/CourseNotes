# -*- coding: utf-8 -*-
"""
Created on Fri May 21 22:27:55 2021

@author: YAG
"""

k=float(input("kilonuz"))
b=float(input("boyunuz"))
bmi= k / (b*b)

print("BMI",bmi)

if bmi<18.5:
    print("Zayıf")
elif 18.5<bmi<25:
    print("Normal")
elif 25<bmi<30:
    print("Kilolu")
elif bmi>30:
    print("obez")
else:
    print("Tutarsız değer")
    
