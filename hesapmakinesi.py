import time as td

def calc():
    intro = """
Yapılacak işlemi seçin\n
-Toplama
-Çıkarma
-Çarpma
-Bölme
-Mod
-Üs Alma
-Karekök
-Çıkış\n
"""


    while True:
        islem = input(intro + ": ")

        if islem == "toplama" or islem == "Toplama":
            num1 = int(input("İlk sayı: "))
            num2 = int(input("İkinci sayı: "))
            res = num1 + num2
            print(f"\nSonuç: {res}")
            td.sleep(1)
            

        elif islem == "çıkarma" or islem == "Çıkarma":
            num1 = int(input("İlk sayı: "))
            num2 = int(input("İkinci sayı: "))
            res = num1 - num2
            print(f"\nSonuç: {res}")
            td.sleep(1)

        elif islem == "çarpma" or islem == "Çarpma":
            num1 = int(input("İlk sayı: "))
            num2 = int(input("İkinci sayı: "))
            res = num1 * num2
            print(f"Sonuç: {res}")
            td.sleep(1)

        elif islem == "bölme" or islem == "Bölme":
            num1 = int(input("İlk sayı: "))
            num2 = int(input("İkinci sayı: "))
            res = num1 / num2
            print(f"\nSonuç: {int(res)}\nKalan: {num1 % num2}")
            td.sleep(1)

        elif islem == "mod" or islem == "Mod":
            num1 = int(input("İlk sayı: "))
            num2 = int(input("İkinci sayı: "))
            res = num1 % num2
            print(f"\nSonuç: {res}")
            td.sleep(1)

        elif islem == "çıkış" or islem == "Çıkış":
            print("\nGoodbye\n")
            td.sleep(1)
            break

        elif islem == "üs" or islem == "Üs" or islem == "üs alma" or islem == "Üs alma":
            num1 = int(input("İlk sayı: "))
            num2 = int(input("İkinci sayı: "))
            res = num1 ** num2
            print(f"\nSonuç: {res}")

        elif islem == "karekök" or islem == "Karekök":
            num1 = int(input("Sayı: "))
            res = num1 ** (1 / 2)
            print(f"\nSonuç: {res}")
        else:
            print("\nLütfen geçerli bir seçenek girin.")
            td.sleep(1)

calc()