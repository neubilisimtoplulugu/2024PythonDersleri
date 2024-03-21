


# Kullanıcıdan alınan bir metni analiz ederek metinde bulunan sesli harflerin ve sessiz harflerin sayısını hesaplayan Python kodunu yazınız.

sesli_harfler = "aeıioöuüAEIİOÖUÜ"
sesli_sayisi = 0
sessiz_sayisi = 0

metin = input("Lütfen bir metin girin: ")

for harf in metin:
    if harf.isalpha(): 
        if harf in sesli_harfler:
            sesli_sayisi += 1
        else:
            sessiz_sayisi += 1
    

print(f"Girdiğiniz metinde {sesli_sayisi} sesli harf ve {sessiz_sayisi} sessiz harf bulunmaktadır.")
