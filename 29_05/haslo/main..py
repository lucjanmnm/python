import random
import string

def generuj_haslo(dlugosc):
    if dlugosc < 4:
        return "Hasło musi mieć przynajmniej 4 znaki!"
    znaki = string.ascii_letters + string.digits + string.punctuation
    haslo = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    haslo += [random.choice(znaki) for _ in range(dlugosc - 4)]
    random.shuffle(haslo)
    return ''.join(haslo)

def main():
    print("Generator silnych haseł")
    try:
        dl = int(input("Podaj długość hasła: "))
        haslo = generuj_haslo(dl)
        print("Twoje hasło:", haslo)
    except ValueError:
        print("Podaj poprawną liczbę całkowitą!")

if __name__ == "__main__":
    main()
