import math
import builtins
def AlanCevre():
    pi = math.pi
    r = int(input("Yarıçap: "))
    alan = (pi * (r ** 2))
    cevre = 2 * pi * r
    print(f"Alan: {alan}, Çevre: {cevre}")

#def Personel():


#def Fib():

# Araba Classları
class Araba:
    def __init__(self, vites, motor, marka, hiz, yakit):
        self.vites = vites
        self.motor = motor
        self.marka = marka
        self.hiz = hiz
        self.yakit = yakit
    
    def marka_ver(self):
        print(f"Marka: {self.marka}")

    def hiz_ver(self):
        print(f"Hız: {self.hiz}")

    def yakit_ver(self):
        print(f"Yakıt: {self.yakit}")

RX7 = Araba("Otomatik", "Wankel Twin Turbo (255 HP)", "Mazda", 251, 10.6)
Challenger = Araba("Manuel", "V8 6.3 (300 HP),", "Dodge", 249, 10.97)
Passat = Araba("Otomatik", "TDI", "Volkswagen", 186, 3.6)

modeller = [RX7, Challenger, Passat]

for araba in modeller:
    araba.marka_ver()
    araba.hiz_ver()
    araba.yakit_ver()
    print("\n")

#Banka Bölümü
class Banka:
    def __init__(self, hesap, miktar, euro, dolar):
        self.hesap, self.miktar, self.euro, self.dolar = hesap, miktar, euro, dolar

    def para_islem(self):
        islem = int(input("Para çekmek için 1, para yatırmak için 2 tuşlayın: "))
        if islem == 1:
            cekmemiktar = int(input("Çekilecek miktarı girin: "))
            if self.miktar < cekmemiktar:
                print("Hesabınızda yeterli bakiye yok. Lütfen tekrar deneyin")
                Banka.para_islem(self)
            else:
                self.miktar -= cekmemiktar
                print(f"Güncel bakiyeniz {self.miktar}")
        
        elif islem == 2:
            yatmamiktar = int(input("Yatırmak istediğiniz miktarı giriniz\n(Normalde para koyulur ama burası dijital): "))
            self.miktar += yatmamiktar
            print(f"Güncel bakiyeniz: {self.miktar}")

    # def havale(self):
    #     print("IBAN Numarası:\n")
    #     iban_giris = int(input("TR"))
    #     if iban_giris == self.iban:
    #         gonderme_miktar = int(input("Gönderilecek miktarı girin: "))
    #         if gonderme_miktar > self.miktar:
    #             print("Hesabınızda istenen miktarda para yok. Lütfen tekrar deneyin.")
    #             Banka.havale(self)
    #         else:
                

    def euroexc(self):
        secim = input("Al/Sat: ")
        secim = secim.lower()
        if secim == "al":
            emiktar = int(input("Alınacak miktar(Euro cinsinden): "))
            if emiktar * 20.2167 < self.miktar:
                self.miktar -= emiktar * 20.2167
                self.euro += emiktar
                print(f"Güncel Bakiye\n{self.miktar} TL, {self.euro} Euro")
            else:
                print("Hesabınızda yeterli para yok. Lütfen tekrar deneyin")
                Banka.euroexc(self)
        
        elif secim == "sat":
            esatis = int(input("Satılacak miktar(Euro cinsinden): "))
            if esatis > self.euro:
                print("Euro hesabınızda yeterli para yok. Lütfen tekrar deneyin")
                Banka.euroexc(self)
            else:
                self.miktar += esatis * 20.2461
                self.euro -= esatis
                print(f"Güncel Bakiye\n{self.miktar} TL, {self.euro} Euro, {self.dolar} Dolar")
        else:
            print("Lütfen geçerli bir seçenek girin.")
            Banka.euroexc(self)

    def dollarexc(self):
        secim = input("Al/Sat: ")
        secim = secim.lower()
        if secim == "al":
            dmiktar = int(input("Alınacak miktar(Dolar cinsinden): "))
            if dmiktar * 18.7729 < self.miktar:
                self.miktar -= dmiktar * 18.7729
                self.dolar += dmiktar
                print(f"Güncel Bakiye:\n {self.miktar} TL, {self.dolar} Dolar, {self.euro} Euro")
            else:
                print("Bankanızda yeterli para yok. Lütfen tekrar deneyin")
                Banka.dollarexc(self)
        elif secim == "sat":
            dsatis = int(input("Satmak istediğiniz miktar(Dolar cinsinden): "))
            if dsatis > self.dolar:
                print("Dolar hesabınızda yeterli miktar yok. Lütfen tekrar deneyin")
                Banka.dollarexc(self)
            else:
                self.dolar -= dsatis
                self.miktar += dsatis * 18.7798
                print(f"Güncel Bakiye:\n {self.miktar} TL, {self.dolar} Dolar, {self.euro} Euro")
        else:
            print("Lütfen geçerli bir seçenek giriniz")
            Banka.dollarexc(self)

    def exchange(self):
        tabela = """
        Dolar: ALIŞ(TL) = 18.7729 --- SATIŞ(TL) = 18.7798
        Euro: ALIŞ(TL) = 20.2167 --- SATIŞ(TL) = 20.2461 
        """
        secim = input("Dolar/Euro: ")
        secim = secim.lower()
        if secim == "euro":
            Banka.euroexc(self)
        elif secim == "dolar":
            Banka.dollarexc(self)
        else:
            print("Lütfen geçerli bir kur seçiniz")
            Banka.exchange(self)





