def suma_parzystych(od, do):
    suma = 0
    for liczba in range(od, do + 1):
        if liczba % 2 == 0:
            suma += liczba
    return suma

# Przykładowe użycie
od = 1
do = 10
wynik = suma_parzystych(od, do)
print(f"Suma liczb parzystych od {od} do {do} wynosi: {wynik}")
