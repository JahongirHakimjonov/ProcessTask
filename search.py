import os

papka_nom = "descriptions"
txt_fayllar = [f for f in os.listdir(papka_nom) if f.endswith(".txt")]

# Izlash uchun so'rovnoma "qidirish kerak bolgan belginingizni kiriting: ""
kerakli_belnidan = '\u0402'

for txt_fayl in txt_fayllar:
    fayl_nom = os.path.join(papka_nom, txt_fayl)

    with open(fayl_nom, 'r') as file:
        malumotlar = file.read()

    boshlangich_pozitsiya = malumotlar.find(kerakli_belnidan)

    if boshlangich_pozitsiya != -1:
        boshlangich_pozitsiya += len(kerakli_belnidan)
        tugash_pozitsiya = malumotlar.find('\n', boshlangich_pozitsiya)

        if tugash_pozitsiya != -1:
            kerakli_belgi = malumotlar[boshlangich_pozitsiya:tugash_pozitsiya]
            print(f"Fayl: {txt_fayl}, Topilgan kerakli belgi: {kerakli_belgi}")
        else:
            print(f"Fayl: {txt_fayl}, Kerakli belgi topilmadi.")
    else:
        print(f"Fayl: {txt_fayl}, Ichidagi.txt faylida kerakli belgi topilmadi.")
