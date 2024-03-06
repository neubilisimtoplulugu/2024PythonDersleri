# SORU 5
# email = input("Email adresinizi girin: ")
# parola = input("Parolanızı girin: ")
# confirmParola = input("Parolanızı tekrar giriniz: ")
# number = "1234567890"
# numberControl = 0


# if "@" in email:
#     if parola == confirmParola:
#         for n in number:
#             if n in parola:
#                numberControl = 1
#                break
#         if numberControl:
#             print("Kayıt başarılı")
#         else:
#             print("Parolanız en az bir sayı içermelidir.")
#     else:
#         print("Parolalar eşit değil.") 
# else:
#     print("Doğru email bilgisi giriniz.")


# dosya = open("kullaniciBilgileri.txt", "w")
# print(email, parola, file=dosya, sep="\n")
# dosya.close()






parola = "5"
confirmParola = "5"
print(id(parola))
print(id(confirmParola))


if parola == confirmParola:
    print("Kayıt başarılı")
else:
    print("Parolalar eşit değil.") 





