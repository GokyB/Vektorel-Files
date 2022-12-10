sayilist = []

def sayi():
    for i in range(10):
        sayinput = int(input("Sayı girin: "))
        sayilist.append(sayinput)
    print(f"\nEn büyük ile en küçük arasındaki fark: {max(sayilist) - min(sayilist)}")

sayi()
