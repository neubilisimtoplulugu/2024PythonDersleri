# SORU 1
# Santigrat olarak verilen sıcaklığı (C) Fahrenhayt’a (F) çeviren bir program yazınız. 
# Yardımcı açıklama: C / 100 = (F-32) / 180

# print(" 1) Santigrat'ı Fahrenayt'a çevir \n 2) Fahrenhayt'ı santigrata çevir")
# secim = int(input("Çevirmek istediğiniz birim seçiniz\n-->"))

# if (secim == 1):
#     c = float(input("C değeri giriniz-->"))
#     f = eval("(c*9/5) + 32")
#     # print(f"{c} santigrat derece --> {f} Fahrenhayt")
#     print("{} santigrat derece --> {} Fahrenhayt".format(c, f))
# else:
#     f = float(input("F değerini giriniz-->"))
#     c = (f-32) * 5/9
#     print(f"{f} fahrenhayt --> {c} santigrat derece")


# print(f"{round(c,2)}")

# round virgülden sonra kaç basamak yazdıracağımızı belirliyor.
#---------------------------------------
# eval örneği
# x = 10
# y = 20
# expr = "x + y * 2"
# sonuc = eval(expr)
# print(sonuc)  # Bu kod 50'yi yazdırır

# expr = input("Bir matematik ifadesi girin: ")
# print("İfade sonucu:", eval(expr))
    
#-------------------------------------------
#random sayı
import random

# 0 ile 100 arasında (dahil) rastgele bir tamsayı üretme
random_integer = random.randint(0, 100,1)
print("Rastgele tamsayı:", random_integer)