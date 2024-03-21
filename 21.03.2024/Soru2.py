

# Bir kullanıcının girdiği metni tersine çeviren ve ardından metinde bulunan kelime sayısını hesaplayan Python kodunu yazınız.


metin = input("Lütfen bir metin girin: ")

# ters_metin = metin[2:5][::-1]
ters_metin = metin[::-1]
print(ters_metin)
kelimeler = ters_metin.split()
kelime_sayisi = len(kelimeler)

print("Metnin tersine çevrilmiş hali:", ters_metin)
print("Metindeki kelime sayısı:", kelime_sayisi)
