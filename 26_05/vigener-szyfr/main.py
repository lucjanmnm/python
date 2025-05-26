def vigenere(text, key, mode='encrypt'):
    result = ""
    key = key.lower()
    key_length = len(key)
    key_int = [ord(i) - ord('a') for i in key]
    for i, char in enumerate(text):
        if char.isalpha():
            k = key_int[i % key_length]
            kod = ord('A') if char.isupper() else ord('a')
            if mode == 'encrypt':
                result += chr((ord(char) - kod + k) % 26 + kod)
            else:  # decrypt
                result += chr((ord(char) - kod - k) % 26 + kod)
        else:
            result += char
    return result

print("Podaj tekst:")
wiadomosc = input("> ")
print("Podaj klucz (np. haslo):")
klucz = input("> ")

print("1. Szyfruj\n2. Deszyfruj")
opcja = input("> ")

if opcja == "1":
    zaszyfrowane = vigenere(wiadomosc, klucz, 'encrypt')
    print("Zaszyfrowany:", zaszyfrowane)
elif opcja == "2":
    odszyfrowane = vigenere(wiadomosc, klucz, 'decrypt')
    print("Odszyfrowany:", odszyfrowane)
else:
    print("Nieznana opcja.")
