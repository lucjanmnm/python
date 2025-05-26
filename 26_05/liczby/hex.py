print("Podaj liczbę szesnastkową (np. 1AF):")
hexa = input("> ")

try:
    dec = int(hexa, 16)
    print("DEC:", dec)
    print("BIN:", bin(dec)[2:])
    print("OCT:", oct(dec)[2:])
except ValueError:
    print("To nie jest poprawna liczba szesnastkowa.")