

import random

key=1

while key==1:
    key = int(input("Oyuna devam etmek için 1, Oyundan çıkmak için 0 yazınız: "))
    if key==0:
        print("Oyundan çıkış yaptınız...")
        key=0
        break
    rastgeldeger = random.randint(1, 50)
    print(rastgeldeger) #Programcı için
    n=0
    while n<5:
        n+=1
        tahmin = int(input("1-50 arasında bir sayı giriniz: "))

        if  tahmin == rastgeldeger :
            print(n, ".Tahminiz doğru :)\nseçilen sayı: ", rastgeldeger)
            break
        elif tahmin > rastgeldeger:
            print(n,". Tahmininiz yanlış, Tahmininiz büyük")
        elif tahmin < rastgeldeger:
            print(n, ". Tahmininiz yanlış, Tahmininiz küçük")

    if n>=5:
        if tahmin != rastgeldeger:
            print("Kaybettin :(\nDoğru sayı",rastgeldeger,"\nTekrar deneyebilirsin")
