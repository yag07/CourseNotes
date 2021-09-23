print(bin(10)) # 2 nin katları

print(hex(100)) # bu sefer 16lık taban

print(round(abs(-10.3))) # mutlak deger ve yuvarlama

# max() ve min() sayıların en büüyk ve küçükleri , sum() toplamları , pow() kuvveti demek


# upper() hepsini büyük yapar , lower() hepsini küçük yapar , replace("a yı","o yapmak") , startswith("p") & endswith("n") başladığı ve bittiği stringi sorgulamak

# split(",") ayırmak için , strip() , lstrip(), rstrip() içine verilen değerlere göre kısaltıyor

# "/".join(liste)

# count("a") kaç defa a var içinde, count("a",2) 2. indexten itibaren sar

# find("a") baştan itibaren arıyor , rfind("a") sondan itiberen arıyor

x = set() # x = {}  boş küme , kümeleri kullanabilmek için listeye çeviriyoruz

x.add(1) # .difference() dersek kümelerin farklarını yazdırıyor , .difference_update() sadece farkları kümeye yazdırıyor

print(x) # .discard() ile kümeden çıkartıyor , intersection() ortak elemanları yazdırıyor , intersection_update()

# isdisjoint() kesişim kümesi var mı? , issubset() alt kümesi mi? , union() birleşim kümesini bulacak

# update() kümeyi birleşim kümesi olarka gücelliyor

# liste.extend(liste2) diğer listeyi ekliyor 

# liste.insert(2,"2. index eklenecek eleman") , liste.pop() , pop(2) 2. indexteki elemanı atacak, liste.remove("Elemanın ismi")

# liste.index(3) 3 elemanının indexini gösterir , liste.index(3,3) 3. indexten itibaren 3 elemanını ara

# liste.count(1) kaç tane  1 var

# liste.sort() , sort(reverse=True)