# SORU 4
# Klavyeden pozitif sayılar girilmektedir. Girilen her sayıdan sonra o ana kadar kaç sayı girildiğini ve girilmiş sayıların ortalamasını görüntüleyen bir program yazınız. Sayı girişi, sıfır veya negatif değer girişi ile sona erecektir ve bu değer, ortalamaya dahil edilmek için geçerli bir değer olarak kabul edilmeyecektir.

toplam = 0
sayac = 0
while True:
    sayi = float(input("Sayi Giriniz"))
    if sayi > 0:
        sayac += 1
        toplam+=sayi
        ort = toplam/sayac
        print(f"Toplam Girilen Sayı Adedi --> {sayac} Ortalama --> {ort}")
    else:
        break


