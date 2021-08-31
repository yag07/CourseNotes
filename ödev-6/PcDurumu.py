import random
import time

class pc():

    def __init__(self, durum = "Kapalı", ses = 0 , program_listesi = ["VSC"] , program = "VSC"):
        
        self.durum = durum

        self.ses   = ses

        self.program_listesi = program_listesi

        self.program = program

    def pc_ac(self):

        if (self.durum == "Açık"):
            print("PC Açık...")
        else:
            print("PC Açılıyor")
            self.durum = "Açık"
    
    def pc_kapa(self):

        if (self.durum == "Kapalı" ):
            print("PC Kapallı")
        else:
            print("PC Kapanıyor")
            self.durum = "Kapalı"

    def ses_ayarla(self):
        while True:

            istek = input("Arttırmak için + ya, eksiltmek için - ye basınız.")

            if (istek == "+"):
                if (self.ses != 100):
                    self.ses  += 1
                    print("Ses: {}".format(self.ses))
            elif (istek == "-"):
                if (self.ses != 0):
                    self.ses -= 1
                    print("Ses: {}".format(self.ses))
            else :
                print("Ses ayarından çıkılıyor. Ses: {} ".format(self.ses))
                break

    def program_ekle(self,program_ismi):
        
        print("{} ekleniyor.".format(program_ismi))

        time.sleep(1)

        self.program_listesi.append(program_ismi)

        print(self.program_listesi)

        return self.program_listesi

    def rastgele_program(self):

        rastgele = random.randint(0,(len(self.program_listesi)-1))

        self.program = self.program_listesi[rastgele]

        print("{} açık olan program.".format(self.program))

    def __len__(self):
        return len(self.program_listesi)
    
    def __str__(self):
        return "Durum: {} \nSes:{} \nProgram Listesi: {} \nProgram: {} ".format(self.durum , self.ses , self.program_listesi , self.program)

PC = pc()

print("""

1-PC Aç

2-PC Kapa

3-Ses Ayarla

4-Program Ekle

5-Program Listesi

6-Rastgele Program

7-Info

Çıkmak için "q"

""")


while True:
    secenek = input("Seçeneği yazınız: ")

    if(secenek == "q"):
        print("Program kapatıldı.")
        break

    elif(secenek == "1"):
        PC.pc_ac()

    elif(secenek == "2"):
        PC.pc_kapa()

    elif(secenek == "3"):
        PC.ses_ayarla()

    elif(secenek == "4"):

        program_isimleri = input("Program isimlerini ',' ile ayırınız.")

        program_listesi = program_isimleri.split(",")

        for ekle in program_listesi:
            PC.program_ekle(ekle)
        
    elif(secenek == "5"):
        print(PC.program_listesi)

    elif(secenek == "6"):
        PC.rastgele_program()

    elif(secenek == "7"):
        print(PC)
        #print(pc)
    else: 
        break