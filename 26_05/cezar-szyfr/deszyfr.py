print("Podaj zaszyfrowany tekst (szyfr Cezara):")
zaszyfrowany = input("> ")

print("\nPróby wszystkich przesunięć:")
for klucz in range(1, 26):
    tekst = ""
    for znak in zaszyfrowany:
        if znak.isalpha():
            kod = ord('A') if znak.isupper() else ord('a')
            tekst += chr((ord(znak) - kod - klucz) % 26 + kod)
        else:
            tekst += znak
    print(f"{klucz}: {tekst}")
