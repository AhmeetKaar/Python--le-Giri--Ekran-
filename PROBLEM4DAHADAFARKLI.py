print("""*******************************************

1'den 100'e kadar olan sayılardan sadece 3'e bölünen sayıları ekrana bastırın.
Bu işlemi continue ile yapmaya çalışın.

*******************************************""")

liste = list(range(0,101))

for i in liste:
    if (i % 3 == 1 or i % 3 == 2):
        continue

    print("i:",i)


