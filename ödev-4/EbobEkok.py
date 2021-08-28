def ebob(i,j):
    k = 1
    ebob = 1
    while (i >= k and j >= k):
        if (not (i % k) and not (j % k)):
            ebob = k
        k += 1
    ekok = ((i*j) / ebob)
    print("EKOK: ", ekok)
    return ebob 

a = int(input("İlk sayıyı giriniz: "))
b= int(input("İkinci sayıyı giriniz: "))

print("EBOB: ",ebob(a,b))
