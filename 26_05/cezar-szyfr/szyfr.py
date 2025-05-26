def szyfruj_cezara(tekst, przesuniecie):
    wynik = ""
    for znak in tekst:
        if znak.isalpha():
            kod = ord('A') if znak.isupper() else ord('a')
            wynik += chr((ord(znak) - kod + przesuniecie) % 26 + kod)
        else:
            wynik += znak
    return wynik

def deszyfruj_cezara(tekst, przesuniecie):
    return szyfruj_cezara(tekst, -przesuniecie)

print("Wybierz opcję:")
print("1. Szyfruj tekst")
print("2. Deszyfruj tekst")
wybor = input("> ")

print("Podaj tekst:")
wiadomosc = input("> ")

print("Podaj przesunięcie (liczbę całkowitą):")
try:
    klucz = int(input("> "))
except ValueError:
    print("To nie jest liczba!")
    exit(1)

if wybor == "1":
    zaszyfrowane = szyfruj_cezara(wiadomosc, klucz)
    print("Zaszyfrowany tekst:", zaszyfrowane)
elif wybor == "2":
    odszyfrowane = deszyfruj_cezara(wiadomosc, klucz)
    print("Odszyfrowany tekst:", odszyfrowane)
else:
    print("Nieznana opcja.")
