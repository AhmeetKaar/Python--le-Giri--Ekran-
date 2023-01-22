print("""
*************************
KULLANICI GİRİŞİ PROGRAMI
*************************
""")

sys_kullanici_adi = "Ahmet"

sys_parola = "12345"

giris_hakki = 3

while True:
    kullanici_adi = input("Kullanıcı Adı:")
    parola = input("Parola:")
    if (kullanici_adi != sys_kullanici_adi and parola == sys_parola):
        print("Kullanıcı Adı Hatalı...")
        giris_hakki -= 1

    elif (kullanici_adi == sys_kullanici_adi and parola != sys_parola):
        print("Parola Hatalı...")
        giris_hakki -= 1

    elif (kullanici_adi != sys_kullanici_adi and parola != sys_parola):
        print("Her İkisi Hatalı...")
        giris_hakki -= 1

    else:
        print("SİSTEME GİRİŞ SAĞLANDI...")
        break
    if (giris_hakki == 0):
        print("GİRİŞ HAKKINIZ BİTTİ...")
        break
