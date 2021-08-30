kj = 1
cal = 4.186 * kj
bg = 1
kw = 1.36*bg
k = 1.4
cv = 0.718 # kj / kg
cp = 1.005 # kj / kg

# v2 / T2 = v3 / T3 sabit basınç
# P4 / T4 = P1 / T1 sabit hacim
# k = cp / cv 
# P1 = 1.8 Bars , T1 = 429 K , rc = 17 

print("Sırayla V1, V2, V3, T1 ve P1 değerlerini giriniz.")

def dizel(v1,v2, v3,T1,P1):
    ko = v1 / v2  # kompresyon oranı
    hao = v3 / v2 # hacim artış oranı
    go = ko / hao # genişleme oranı
  
    T2 = T1*(ko**(k-1))
    P2 = P1*((ko)**(k))

    T3 = T1*hao*(ko**(k-1))
    P3 = P2

    T4 = T1*(hao**(k))
    P4 = P1*((hao)**(k))

    v = (1-((1/(ko**(k-1)))*(((hao**(k))-1)/(k*(hao-1)))))

    print("Kompresyon oranı: ", ko)
    print("Hacim artış oranı: ", hao)  
    print("Genişleme oranı: ", go) 
    print("T2: {} K, T3: {} K, T4: {} K ".format(T2,T3,T4))
    print("P2: {} , P3: {} , P4: {} ".format(P2,P3,P4))
    print("Verim: {} ".format(v))

    return P3 , v