import random

def rozdanie_karty():
    karty = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    return random.choice(karty)

def wartosc_karty(karta):
    if karta in ['J', 'Q', 'K']:
        return 10
    if karta == 'A':
        return 11
    return int(karta)

def suma_kart(reka):
    suma = 0
    asy = 0
    for karta in reka:
        if karta == 'A':
            asy += 1
        suma += wartosc_karty(karta)
    while suma > 21 and asy:
        suma -= 10
        asy -= 1
    return suma

def pokaz_reke(gracz, reka, ukryta=False):
    if ukryta:
        print(f"{gracz}: [{reka[0]}] [ukryta]")
    else:
        print(f"{gracz}: {' '.join(reka)} (suma: {suma_kart(reka)})")

def blackjack():
    saldo = 100
    print("Witaj w Blackjacku (Oczko)!")
    print("Masz 100 żetonów.")
    while saldo > 0:
        print(f"\nTwój stan żetonów: {saldo}")
        try:
            stawka = int(input("Podaj stawkę (min. 1, max. 50, 0 aby zakończyć): "))
            if stawka == 0:
                print("Kończysz grę z", saldo, "żetonami. Dzięki!")
                break
            if stawka < 1 or stawka > 50 or stawka > saldo:
                print("Nieprawidłowa stawka!")
                continue
        except ValueError:
            print("Podaj liczbę!")
            continue

        twoja_reka = [rozdanie_karty(), rozdanie_karty()]
        dealer_reka = [rozdanie_karty(), rozdanie_karty()]

        pokaz_reke("Twoja ręka", twoja_reka)
        pokaz_reke("Krupier", dealer_reka, ukryta=True)

        while True:
            if suma_kart(twoja_reka) == 21:
                print("Blackjack! Masz 21!")
                break
            wybor = input("Dobierasz kartę? (t/n): ").lower()
            if wybor == 't':
                twoja_reka.append(rozdanie_karty())
                pokaz_reke("Twoja ręka", twoja_reka)
                if suma_kart(twoja_reka) > 21:
                    print("Przegrałeś - przekroczyłeś 21!")
                    saldo -= stawka
                    break
            elif wybor == 'n':
                break
            else:
                print("Odpowiedz t (tak) lub n (nie).")
        else:
            continue 

        if suma_kart(twoja_reka) > 21:
            continue

        pokaz_reke("Krupier", dealer_reka)
        while suma_kart(dealer_reka) < 17:
            print("Krupier dobiera kartę...")
            dealer_reka.append(rozdanie_karty())
            pokaz_reke("Krupier", dealer_reka)

        suma_gracza = suma_kart(twoja_reka)
        suma_krupiera = suma_kart(dealer_reka)

        if suma_krupiera > 21:
            print("Krupier przekroczył 21! Wygrywasz!")
            saldo += stawka
        elif suma_gracza > suma_krupiera:
            print("Wygrywasz!")
            saldo += stawka
        elif suma_gracza < suma_krupiera:
            print("Przegrywasz :(")
            saldo -= stawka
        else:
            print("Remis!")

    if saldo <= 0:
        print("Przegrałeś wszystkie żetony! Koniec gry.")

blackjack()
