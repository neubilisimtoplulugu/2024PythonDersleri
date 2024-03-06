# SORU 3
# Verilen a ve d değerleri için N elemanlı aritmetik diziyi hesaplayıp görüntüleyen bir program yazınız. Aritmetik dizi: a, a+d, a+2d, a+3d, a+4d, ... , a+(N-1)d

a = float(input("Başlangıç değeri girin --> "))
d = float(input("Artış miktarı girin --> "))

N = int(input("Eleman sayısı girin --> "))
for x in range(1, N+1):
    sonuc = a + (x-1) * d
    print("Aritmetik dizi {}.eleman : {}".format(x,sonuc))

    