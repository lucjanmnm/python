print("Podaj liczbę dziesiętną:")
dec = input("> ")

try:
    dec = int(dec)
    print("BIN:", bin(dec)[2:])
    print("OCT:", oct(dec)[2:])
    print("HEX:", hex(dec)[2:].upper())
except ValueError:
    print("To nie jest poprawna liczba dziesiętna.")