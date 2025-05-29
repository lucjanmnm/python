import random

odpowiedzi = {
    "cześć": "Cześć! Jak mogę Ci pomóc?",
    "hej": "Hej! Co słychać?",
    "witaj": "Witaj! Jak się masz?",
    "jak masz na imię": "Jestem PythonBot!",
    "jak się masz": "Mam się świetnie, dzięki!",
    "co potrafisz": "Potrafię odpowiadać na proste pytania!",
    "do widzenia": "Do zobaczenia! Miłego dnia!"
}

inne_odpowiedzi = [
    "Hmm, nie wiem co odpowiedzieć.",
    "Ciekawe pytanie!",
    "Niestety, nie znam odpowiedzi.",
    "Możesz zapytać o coś innego?"
]

print("Cześć! Jestem prostym chatbotem. Zapytaj mnie o coś (wpisz 'do widzenia', żeby zakończyć).")

while True:
    pytanie = input("Ty: ").lower()
    if pytanie in odpowiedzi:
        print("Bot:", odpowiedzi[pytanie])
        if pytanie == "do widzenia":
            break
    else:
        print("Bot:", random.choice(inne_odpowiedzi))
