class laptop():
    def __init__(self,marka,ssd,ram):
        print("Laptop bilgileri __init__ edildi.")
        self.marka = marka
        self.ssd   = ssd
        self.ram   = ram
    
    def goster(self):
        print("""
        
        Marka : {} 

        Ssd   : {}

        Ram   : {}

        """.format(self.marka,self.ssd,self.ram))

    def yukseltme(self,ssdy,ramy):
        print("Yükseltmeler ekleniyor")
        self.ssd = ssdy
        self.ram = ramy

    def __str__(self):
        return "Marka: {} , Ssd: {} , Ram: {} ".format(self.marka,self.ssd,self.ram)

    def __del__(self):
        print("Class'a ait obje siliniyor")

class parcalar(laptop):
    #pass
    def __init__(self,marka,ssd,ram,ekran):
        super().__init__(marka,ssd,ram)
        print("Parça bilgileri kaydedildi.")
        self.ekran = ekran
        
mylaptop = laptop("Asus", 512 , 16)

mylaptop.goster()

mylaptop.yukseltme("1 TB" , 32)

mylaptop.goster()

print(mylaptop) # str fonkiyon metodu

myparcalar = parcalar("ROG", "Samsung", "16 GB" ,"FHD")

myparcalar.goster()

del myparcalar

mylaptop.goster()

# myparcalar.goster() silindiği için görünmeyecek

