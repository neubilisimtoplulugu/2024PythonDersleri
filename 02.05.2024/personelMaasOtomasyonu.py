'''

1) maas_hesapla(brut_ucret, haftalik_calisma_saati): Haftalık çalışma saati ve brüt ücret alarak bir personelin haftalık net maaşını hesaplar. Haftalık çalışma saati 40 saatten azsa normal saatlik ücretle, 40 saatten fazla ise fazla mesai ücretiyle hesaplanır. Ardından vergi kesintisi yapılır ve net maaş döndürülür.
2) calisma_saati_kaydet(): Kullanıcıdan haftalık çalışma saati bilgisini alır ve onu bir ondalık sayı olarak döndürür.
3)yeni_personel_ekle(personeller, brut_ucret): Kullanıcıdan yeni bir personelin adını ve haftalık çalışma saatini alır, bu bilgilerle bir personel sözlüğü oluşturur ve bu sözlüğü personeller listesine ekler.
4) personel_listele(personeller): Personel listesini alır ve her bir personelin adını, haftalık çalışma saatini ve brüt ücretini ekrana yazdırır.
5) main(): Programın ana döngüsüdür. Kullanıcıya bir dizi seçenek sunar: yeni personel eklemek, çalışma saatlerini kaydetmek, maaşı hesaplamak veya programdan çıkmak. Kullanıcının seçimine göre ilgili işlevler çağrılır ve program ilerler.

'''



def maas_hesapla(brut_ucret, haftalik_calisma_saati):
    normal_calisma_saati = 40
    normal_maas = normal_calisma_saati * brut_ucret
    fazla_mesai_ucreti = 1.5 * brut_ucret

    if haftalik_calisma_saati <= normal_calisma_saati:
        maas = haftalik_calisma_saati * brut_ucret
    else:
        normal_maas = normal_calisma_saati * brut_ucret
        fazla_mesai_maasi = (haftalik_calisma_saati - normal_calisma_saati) * fazla_mesai_ucreti
        maas = normal_maas + fazla_mesai_maasi

    vergi_orani = 0.25
    vergi_miktari = maas * vergi_orani
    net_maas = maas - vergi_miktari

    return net_maas

def calisma_saati_kaydet():
    haftalik_calisma_saati = float(input("Haftalık çalışma saatinizi girin: "))
    return haftalik_calisma_saati

def yeni_personel_ekle(personeller, brut_ucret):
    ad = input("Yeni personelin adını girin: ")
    haftalik_calisma_saati = calisma_saati_kaydet()
    personel = {"ad": ad,"brut_ucret": brut_ucret,"haftalik_calisma_saati": haftalik_calisma_saati}
    personeller.append(personel)
    print(f"{ad} adlı personel başarıyla eklendi.")

def personel_listele(personeller):
    i = 0
    for personel in personeller:
        print(f"{i}.Personel Ad: {personel['ad']}, Haftalık Çalışma Saati: {personel['haftalik_calisma_saati']}, Brüt Ücret: {personel['brut_ucret']}\n-------------------------------")

def main():
    brut_ucret = float(input("Tüm personeller için saatlik brüt ücreti girin: "))
    personeller = []

    while True:
        print("\n*** MAAŞ HESAPLAMA OTOMASYONU ***")
        print("1. Yeni Personel Ekle")
        print("2. Çalışma Saati Kaydet")
        print("3. Maaşı Hesapla")
        print("4. Çıkış")

        secim = input("Yapmak istediğiniz işlemi seçin (1/2/3/4): ")

        if secim == "1":
            yeni_personel_ekle(personeller, brut_ucret)
        elif secim == "2":
            if not personeller:
                print("Önce bir personel eklemelisiniz.")
                continue
            personel_listele(personeller)
            personel_index = int(input("Çalışma saatlerini kaydetmek istediğiniz personelin indeksini girin: "))
            if personel_index < 0 or personel_index >= len(personeller):
                print("Geçersiz personel indeksi.")
                continue

            personeller[personel_index]["haftalik_calisma_saati"] = calisma_saati_kaydet()
            print(f"{personeller[personel_index]['ad']} adlı personelin çalışma saatleri güncellendi.")
        elif secim == "3":
            if not personeller:
                print("Önce bir personel eklemelisiniz.")
                continue
            personel_listele(personeller)
            personel_index = int(input("Maaşını hesaplamak istediğiniz personelin indeksini girin: "))
            if personel_index < 0 or personel_index >= len(personeller):
                print("Geçersiz personel indeksi.")
                continue
            net_maas = maas_hesapla(brut_ucret, personeller[personel_index]["haftalik_calisma_saati"])
            print(f"{personeller[personel_index]['ad']} adlı personelin haftalık net maaşı: {net_maas} TL")
        elif secim == "4":
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz bir seçim yaptınız. Lütfen tekrar deneyin.")

main()
