print("Podaj liczbę ósemkową (np. 127):")
octal = input("> ")

try:
    dec = int(octal, 8)
    print("DEC:", dec)
    print("BIN:", bin(dec)[2:])
    print("HEX:", hex(dec)[2:].upper())
except ValueError:
    print("To nie jest poprawna liczba ósemkowa.")