print("""*******************************************

1'den 100'e kadar olan sayılardan sadece 3'e bölünen sayıları ekrana bastırın.
Bu işlemi continue ile yapmaya çalışın.

*******************************************""")

while True:
    sayı = int(input("Lütfen 100'e Kadar Bir Sayı Giriniz:"))

    if(sayı % 3 == 1 ):
        print("3 İle Bölümünden Kalan 1'dir")


    elif(sayı % 3 == 2):
        print("3 İle Bölümünden Kalan 2'dir.")


    else:
        print("3'e Tam Bölünür.")
