score = {"a": 1, "b": 3, "c": 3, "d": 2,
         "e": 1, "f": 4, "g": 2, "h": 4,
         "i": 1, "j": 8, "k": 5, "l": 1,
         "m": 3, "n": 1, "o": 1, "p": 3,
         "q": 10, "r": 1, "s": 1, "t": 1,
         "u": 1, "v": 4, "w": 4, "x": 8,
         "y": 4, "z": 10}


def scrable_score(word):
    total_score = 0
    for letter in word.lower():
        total_score += score[letter]
    return total_score


if __name__ == '__main__':
    while True:
        my_word = input('Podaj wyraz: ').strip()
        wynik = scrable_score(my_word)
        print('Wynik działania programu')
        print(f'Słowo {my_word} jest warte {wynik} w Scrable')
        shall_continue = input('Czy chcesz kont T/N: ')
        if shall_continue.lower() != 't':
            break
