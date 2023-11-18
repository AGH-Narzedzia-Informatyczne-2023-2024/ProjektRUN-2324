import random

def zgaduj_liczbe():
    dolna_granica = 1
    gorna_granica = 10
    liczba = random.randint(dolna_granica, gorna_granica)
    proba = 1

    while True:
        print(f"Próba {proba}: Zgaduję, że liczba to {liczba}")
        odpowiedz = input("Czy to jest poprawna liczba? (t/n): ")

        if odpowiedz.lower() == "t":
            print(f"Hurra! Zgadłem liczbę {liczba} po {proba} próbach!")
            break
        elif odpowiedz.lower() == "n":
            wskazowka = input("Czy liczba jest za duża czy za mała? (d/m): ")
            if wskazowka.lower() == "d":
                gorna_granica = liczba - 1
            elif wskazowka.lower() == "m":
                dolna_granica = liczba + 1

        liczba = random.randint(dolna_granica, gorna_granica)
        proba += 1

zgaduj_liczbe()
