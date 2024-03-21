



# Rastgele üretilen sayılar arasındaki minimum farkı bulan bir Python programı yazın.
# Program, 1 ile 100 arasında rastgele sayılar üretecek ve ardından bu sayılar arasındaki minimum farkı bulacak. Random sayı 40 ile 80 arasında ise döngü sonlanacak.


import random

min_fark = 100
sayi1 = 0

while True:

    random_sayi = random.randint(1, 100)
    print(random_sayi)

   

    if sayi1 != 0:
        fark = abs(sayi1 - random_sayi) # Mutlak değer fonksiyonu abs()  
        if fark < min_fark:
            min_fark = fark

    sayi1 = random_sayi
    
    if 75 <= random_sayi <= 80:
        break


print("Minimum Fark:", min_fark)
