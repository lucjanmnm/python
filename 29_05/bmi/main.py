def bmi():
    try:
        waga = float(input("Podaj swoją wagę w kg: ").replace(",", "."))
        wzrost_cm = float(input("Podaj swój wzrost w centymetrach: ").replace(",", "."))
        wzrost_m = wzrost_cm / 100
        bmi = waga / (wzrost_m ** 2)
        print(f"Twoje BMI: {bmi:.2f}")
        if bmi < 18.5:
            print("Niedowaga")
        elif bmi < 25:
            print("Waga prawidłowa")
        elif bmi < 30:
            print("Nadwaga")
        else:
            print("Otyłość")
    except ValueError:
        print("Podano nieprawidłowe dane.")

bmi()
