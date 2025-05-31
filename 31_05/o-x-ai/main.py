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

def ruch_poprawny(plansza, pole):
    if pole < 1 or pole > 9:
        return False
    w, k = (pole - 1) // 3, (pole - 1) % 3
    return plansza[w][k] not in ["X", "O"]

def zamien_liczby_na_puste(plansza):
    for i in range(3):
        for j in range(3):
            if plansza[i][j] not in ["X", "O"]:
                plansza[i][j] = " "

def dostepne_ruchy(plansza):
    return [(i, j) for i in range(3) for j in range(3) if plansza[i][j] not in ["X", "O"]]

def plansza_pelna(plansza):
    return all(plansza[i][j] in ["X", "O"] for i in range(3) for j in range(3))

def minimax(plansza, depth, is_maximizing):
    if sprawdz_wygrana(plansza, "O"):
        return 1
    if sprawdz_wygrana(plansza, "X"):
        return -1
    if plansza_pelna(plansza):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for (i, j) in dostepne_ruchy(plansza):
            plansza[i][j] = "O"
            score = minimax(plansza, depth + 1, False)
            plansza[i][j] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for (i, j) in dostepne_ruchy(plansza):
            plansza[i][j] = "X"
            score = minimax(plansza, depth + 1, True)
            plansza[i][j] = " "
            best_score = min(score, best_score)
        return best_score

def ruch_komputera(plansza):
    best_score = -float('inf')
    best_move = None
    for (i, j) in dostepne_ruchy(plansza):
        plansza[i][j] = "O"
        score = minimax(plansza, 0, False)
        plansza[i][j] = " "
        if score > best_score:
            best_score = score
            best_move = (i, j)
    return best_move

def gra_kolko_krzyzyk_vs_ai():
    plansza = [[str(i * 3 + j + 1) for j in range(3)] for i in range(3)]
    ruchy = 0
    pierwszy_ruch = True
    while ruchy < 9:
        wyswietl_plansze(plansza)
        while True:
            try:
                pole = int(input("Twój ruch (podaj numer pola 1-9): "))
                if not ruch_poprawny(plansza, pole):
                    print("Nieprawidłowy ruch, spróbuj jeszcze raz.")
                    continue
                w, k = (pole - 1) // 3, (pole - 1) % 3
                plansza[w][k] = "X"
                ruchy += 1
                if pierwszy_ruch:
                    zamien_liczby_na_puste(plansza)
                    pierwszy_ruch = False
                break
            except ValueError:
                print("Wpisz LICZBĘ od 1 do 9.")
        if sprawdz_wygrana(plansza, "X"):
            wyswietl_plansze(plansza)
            print("Wygrałeś!")
            return
        if ruchy == 9:
            break
        print("Ruch komputera (O):")
        ruch = ruch_komputera(plansza)
        if ruch is None:
            break
        w, k = ruch
        plansza[w][k] = "O"
        ruchy += 1
        print(f"Komputer wybrał pole {(w * 3 + k + 1)}")
        if sprawdz_wygrana(plansza, "O"):
            wyswietl_plansze(plansza)
            print("Komputer wygrał!")
            return
    wyswietl_plansze(plansza)
    print("Remis!")

gra_kolko_krzyzyk_vs_ai()
