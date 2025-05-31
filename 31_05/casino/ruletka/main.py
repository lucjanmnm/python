import random

def ruletka():
    saldo = 100
    print("Masz 100 żetonów.")

    while saldo > 0:
        print(f"\nTwój stan żetonów: {saldo}")
        try:
            stawka = int(input("Podaj stawkę (min. 1, max. 50, 0 by zakończyć): "))
            if stawka == 0:
                print("Opuszczasz stół ruletki z", saldo, "żetonami. Dzięki za grę!")
                break
            if stawka < 1 or stawka > 50 or stawka > saldo:
                print("Nieprawidłowa stawka!")
                continue
        except ValueError:
            print("Podaj liczbę!")
            continue

        typ = input("Obstaw kolor (czerwony/czarny/zielony): ").strip().lower()
        if typ not in ["czerwony", "czarny", "zielony"]:
            print("Błędny kolor! Wybierz: czerwony, czarny lub zielony.")
            continue

        wynik = random.randint(0, 36)
        if wynik == 0:
            kolor = "zielony"
        elif wynik % 2 == 0:
            kolor = "czarny"
        else:
            kolor = "czerwony"

        print(f"Na ruletce wypadło: {wynik} ({kolor})")

        if typ == kolor:
            if kolor == "zielony":
                wygrana = stawka * 14
                print("TRAFIŁEŚ ZIELONE! Wygrywasz", wygrana, "żetonów!")
            else:
                wygrana = stawka * 2
                print("Trafiłeś kolor! Wygrywasz", wygrana, "żetonów!")
            saldo += wygrana
        else:
            print("Przegrywasz stawkę :(")
            saldo -= stawka

    if saldo <= 0:
        print("Nie masz już żetonów. Koniec gry!")

ruletka()
