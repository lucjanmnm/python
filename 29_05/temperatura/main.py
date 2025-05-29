def konwerter_temperatury():
    try:
        c = float(input("Podaj temperaturę w °C: "))
        f = c * 9/5 + 32
        k = c + 273.15
        print(f"{c}°C = {f:.2f}°F = {k:.2f}K")
    except ValueError:
        print("Podano nieprawidłową wartość.")
konwerter_temperatury()
