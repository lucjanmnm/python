import difflib

correct_words = ["pies", "kot", "słoń", "lew", "papuga"]

user_input = input("Podaj 1 zwierze (pies, kot, słoń, lew, papuga): ")

matches = difflib.get_close_matches(user_input, correct_words, n=1, cutoff=0.7)

if matches:
    print(f"Czy chodziło Ci o: {matches[0]}?")
else:
    print("Nie znaleziono podobnego słowa.")

for word in correct_words:
    similarity = difflib.SequenceMatcher(None, user_input, word).ratio()
    print(f"Podobieństwo '{user_input}' do '{word}': {similarity:.2f}")