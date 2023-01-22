print("""***************************************

Problem 1
Kullanıcıdan aldığınız bir sayının mükemmel olup olmadığını bulmaya çalışın.

Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükemmel sayı" denir.
Örnek olarak, 6 mükemmel bir sayıdır. (1 + 2 + 3 = 6)


***************************************""")


sayı = int(input("Lütfen Bir Sayı Giriniz: "))

i = 1
x = 0

while (i < sayı):
    if (sayı % i == 0):
        x += i

    i += 1

if (x == sayı):
    print(sayı,"mükemmel bir sayıdır.")

else:
    print(sayı,"mükemmmel sayı değildir.")


