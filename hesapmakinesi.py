import time as td

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def calc():
    intro ="""
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

    try:
        while True:
            islem = input(intro + ": ")

            if islem == "toplama" or islem == "Toplama":
                num1 = int(input("İlk sayı: "))
                num2 = int(input("İkinci sayı: "))
                res = num1 + num2
                print(f"\n{bcolors.BOLD}{bcolors.OKGREEN}Sonuç: {res}{bcolors.ENDC}")
                td.sleep(1)
            

            elif islem == "çıkarma" or islem == "Çıkarma":
                num1 = int(input("İlk sayı: "))
                num2 = int(input("İkinci sayı: "))
                res = num1 - num2
                print(f"\n{bcolors.BOLD}{bcolors.OKGREEN}Sonuç: {res}{bcolors.ENDC}")
                td.sleep(1)

            elif islem == "çarpma" or islem == "Çarpma":
                num1 = int(input("İlk sayı: "))
                num2 = int(input("İkinci sayı: "))
                res = num1 * num2
                print(f"\n{bcolors.BOLD}{bcolors.OKGREEN}Sonuç: {res}{bcolors.ENDC}")
                td.sleep(1)

            elif islem == "bölme" or islem == "Bölme":
                num1 = int(input("İlk sayı: "))
                num2 = int(input("İkinci sayı: "))
                res = num1 / num2
                print(f"\n{bcolors.BOLD}{bcolors.OKGREEN}Sonuç: {int(res)}\nKalan: {num1 % num2}{bcolors.ENDC}")
                td.sleep(1)

            elif islem == "mod" or islem == "Mod":
                num1 = int(input("İlk sayı: "))
                num2 = int(input("İkinci sayı: "))
                res = num1 % num2
                print(f"\n{bcolors.BOLD}{bcolors.OKGREEN}Sonuç: {res}{bcolors.ENDC}")
                td.sleep(1)

            elif islem == "çıkış" or islem == "Çıkış":
                print(f"\n{bcolors.BOLD}{bcolors.BOLD}GOODBYE{bcolors.ENDC}\n")
                td.sleep(1)
                break

            elif islem == "üs" or islem == "Üs" or islem == "üs alma" or islem == "Üs alma":
                num1 = int(input("İlk sayı: "))
                num2 = int(input("İkinci sayı: "))
                res = num1 ** num2
                print(f"\n{bcolors.BOLD}{bcolors.BOLD}Sonuç: {res}{bcolors.ENDC}")

            elif islem == "karekök" or islem == "Karekök":
                num1 = int(input("Sayı: "))
                res = num1 ** (1 / 2)
                print(f"\n{bcolors.BOLD}{bcolors.OKGREEN}Sonuç: {res}{bcolors.ENDC}")
            else:
                print(f"\n{bcolors.BOLD}{bcolors.WARNING}Lütfen geçerli bir seçenek girin.{bcolors.ENDC}")
                td.sleep(1)
    except ValueError as hata:
        print(f"\n{bcolors.BOLD}{bcolors.FAIL}Lütfen sadece sayı girin ({hata}){bcolors.ENDC}\n")
        calc()
    except ZeroDivisionError as hata:
        print(f"\n{bcolors.BOLD}{bcolors.FAIL}SIFIRLA BÖLME HATASI ({hata}){bcolors.ENDC}\n")
        calc()

calc()
