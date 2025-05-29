def wyswietl_plansze(plansza):
    for i in range(3):
        print(" | ".join(plansza[i]))
        if i < 2:
            print("-" * 9)

def sprawdz_wygrana(plansza, gracz):
    for i in range(3):
        if all(plansza[i][j] == gracz for j in range(3)):
            return True
        if all(plansza[j][i] == gracz for j in range(3)):
            return True
    if all(plansza[i][i] == gracz for i in range(3)):
        return True
    if all(plansza[i][2 - i] == gracz for i in range(3)):
        return True
    return False

def ruch_poprawny(plansza, w, k):
    return 0 <= w < 3 and 0 <= k < 3 and plansza[w][k] == " "

def gra_kolko_krzyzyk():
    plansza = [[" " for _ in range(3)] for _ in range(3)]
    gracz = "X"
    for ruch in range(9):
        wyswietl_plansze(plansza)
        print(f"Ruch gracza {gracz}")
        try:
            w = int(input("Podaj wiersz (0-2): "))
            k = int(input("Podaj kolumnę (0-2): "))
            if not ruch_poprawny(plansza, w, k):
                print("Nieprawidłowy ruch, spróbuj jeszcze raz.")
                continue
            plansza[w][k] = gracz
            if sprawdz_wygrana(plansza, gracz):
                wyswietl_plansze(plansza)
                print(f"Gracz {gracz} wygrywa!")
                return
            gracz = "O" if gracz == "X" else "X"
        except ValueError:
            print("Wpisz liczbę od 0 do 2.")
    wyswietl_plansze(plansza)
    print("Remis!")

gra_kolko_krzyzyk()
