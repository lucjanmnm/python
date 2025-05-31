import random

def slot_machine():
    symbole = ["🍒", "🔔", "🍋", "⭐", "7️⃣"]
    saldo = 100
    print("Masz 100 żetonów.")
    
    while saldo > 0:
        print(f"\nTwój aktualny stan żetonów: {saldo}")
        try:
            stawka = int(input("Podaj stawkę (min. 1, max. 20, 0 aby zakończyć): "))
            if stawka == 0:
                print("Dzięki za grę! Zostało Ci", saldo, "żetonów.")
                break
            if stawka < 1 or stawka > 20 or stawka > saldo:
                print("Nieprawidłowa stawka!")
                continue
        except ValueError:
            print("Podaj liczbę!")
            continue

        wynik = [random.choice(symbole) for _ in range(3)]
        print(" | ".join(wynik))

        if wynik.count(wynik[0]) == 3:
            wygrana = stawka * 10
            print("JACKPOT! Trzy takie same! Wygrywasz", wygrana, "żetonów!")
            saldo += wygrana
        elif wynik.count(wynik[0]) == 2 or wynik.count(wynik[1]) == 2:
            wygrana = stawka * 2
            print("Dwie takie same! Wygrywasz", wygrana, "żetonów!")
            saldo += wygrana
        else:
            print("Nic nie wygrałeś :(")
            saldo -= stawka

    if saldo <= 0:
        print("Przegrałeś wszystkie żetony! Koniec gry.")

slot_machine()
