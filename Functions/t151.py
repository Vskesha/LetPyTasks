def encrypt (s, k):
    letters = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    i = k % len(letters)
    letters_mod = letters[i:] + letters[:i]
    table = s.upper().maketrans(letters, letters_mod)
    return s.upper().translate(table)
