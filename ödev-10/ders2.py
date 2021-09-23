class Dosya():

    def __init__(self):

        with open("şiir.txt","r",encoding="utf-8") as file:

            icerik = file.read()

            kelime = icerik.split()

            self.kelimeler = list()

            for i in kelime:

                i = i.strip("\n")
                i = i.strip(" ")
                i = i.strip(".")
                i = i.strip(",")

                self.kelimeler.append(i)

            for i in self.kelimeler:
                print(i)
    
    def tum_kelimeler(self):

        kelime_kumesi = set()

        for i in self.kelimeler:

            kelime_kumesi.add(i)
        
        print("***************************Tüm kelimeler************************")

        for i in kelime_kumesi:

            print(i)

    def kelime_frekansı(self):

        kelime_sözlük = dict()

        print("*****************************************************************")

        for i in self.kelimeler:
            
            if (i in kelime_sözlük):

                kelime_sözlük[i] += 1

            else:
                
                kelime_sözlük[i] = 1

        for kelime, defa in kelime_sözlük.items():

            print(f"{kelime}  --- kelimesi, {defa} defa geçiyor. ")

dosya = Dosya()

dosya.tum_kelimeler()

dosya.kelime_frekansı()