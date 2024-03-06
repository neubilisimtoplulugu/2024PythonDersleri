# SORU 2
# F1 tamsayı değerinden F2 değerine kadar fahrenhayt sıcaklık değerlerini birer artırarak fahrenhayt-santigrat tablosu hazırlayan bir program yazınız.

print("1)Fahrenhayt\n2)Santigrat")

secim = input("Çevirmek istediğniz birim seçiniz --> ")
print(type(secim))
if secim == "1":
    f1 = int(input("Fahrenhayt başlangıç değeri --> "))
    f2 = int(input("Fahrenhayt bitiş değeri --> "))
    print("Değer    Sonuç ")
    for x in range(f1, f2+1, 2):
        sonuc = 5*(x-32)/9
        print(f"  {x}   {sonuc:.2f}")
    
elif secim == "2":
    c1 = int(input("Santigrat başlangıç değeri --> "))
    c2 = int(input("Santigrat bitiş değeri --> "))
    print("Değer\t Sonuç ")

    for x in range(c1,c2+1):
        x = 9*(x/5)+32
        print(f"  {c1}\t  {x:.2f}")
       
else:
    print("--> Hatalı Seçim Yaptınız <--")


    
