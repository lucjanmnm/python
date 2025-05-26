print("Podaj dowolne zdanie:")
zdanie = input("> ")

samogloski = "aeiouyąęAEIOUYĄĘ"
licznik = 0

for znak in zdanie:
    if znak in samogloski:
        licznik += 1

print(f"Liczba samogłosek w podanym zdaniu: {licznik}")
