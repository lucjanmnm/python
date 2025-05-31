import time
import random

def test_refleksu():
    print("Za chwilę pojawi się sygnał 'Naciśnij Enter!'. Wciśnij Enter najszybciej jak potrafisz.")
    print("Przygotuj się...")
    time.sleep(random.uniform(2, 5))
    print("Naciśnij Enter!")
    start = time.time()
    input()
    koniec = time.time()
    czas = koniec - start
    print(f"Twój czas reakcji: {czas:.3f} sekundy.")
    if czas < 0.2:
        print("Masz refleks jak ninja! 🚀")
    elif czas < 0.35:
        print("Świetny wynik!")
    elif czas < 0.5:
        print("Całkiem nieźle.")
    else:
        print("Spróbuj jeszcze raz – może będzie szybciej :)")

test_refleksu()
