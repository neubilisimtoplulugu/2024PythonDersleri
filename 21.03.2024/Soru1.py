


# Verilen bir metindeki harflerin ve rakamların sayısını hesaplayan bir Python programı yazın. Program, kullanıcıdan bir metin dizisi alacak ve sonra metindeki harf ve rakamların toplam sayısını ekrana yazdıracaktır. Boşluklar ve diğer özel karakterler sayılmayacaktır.


harf_sayisi = 0
rakam_sayisi = 0

metin = input("Lütfen bir metin girin: ")

for karakter in metin:
    if karakter.isalpha():
        harf_sayisi += 1    
    elif karakter.isdigit():
        rakam_sayisi += 1
    

print("Metindeki harf sayısı:", harf_sayisi)
print("Metindeki rakam sayısı:", rakam_sayisi)
