print("Podaj liczbę binarną (np. 101101):")
binarny = input("> ")

try:
    dec = int(binarny, 2)
    print("DEC:", dec)
    print("OCT:", oct(dec)[2:])
    print("HEX:", hex(dec)[2:].upper())
except ValueError:
    print("To nie jest poprawna liczba binarna.")