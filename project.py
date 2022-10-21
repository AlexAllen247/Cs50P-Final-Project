from random import sample
from collections import Counter
from sys import exit


def main():
    random_letters()
    user_input = str(input("What is your word: ").strip().lower())
    check = check_word(user_input)
    points = word_score(check)
    print(f"{points} points, Well Done!")


def random_letters():
    letters = Counter(
        a=9,
        b=2,
        c=2,
        d=4,
        e=12,
        f=2,
        g=3,
        h=2,
        i=9,
        j=1,
        k=1,
        l=4,
        m=2,
        n=6,
        o=8,
        p=2,
        q=1,
        r=6,
        s=4,
        t=6,
        u=4,
        v=2,
        w=2,
        x=1,
        y=2,
        z=1,
    )
    list_of_letters = list(sorted(letters.elements()))
    hand = sample(list_of_letters, 7)
    print(hand)


def check_word(user_input):
    with open("Collins Scrabble Words (2019).txt") as file:
        words = set(word.strip().lower() for word in file)
        if user_input in words:
            return user_input
        else:
            exit("Unfortunately that is not a word, better luck next time!")


def word_score(user_input):
    score = {
        "a": 1,
        "b": 3,
        "c": 3,
        "d": 2,
        "e": 1,
        "f": 4,
        "g": 2,
        "h": 4,
        "i": 1,
        "j": 8,
        "k": 5,
        "l": 1,
        "m": 3,
        "n": 1,
        "o": 1,
        "p": 3,
        "q": 10,
        "r": 1,
        "s": 1,
        "t": 1,
        "u": 1,
        "v": 4,
        "w": 4,
        "x": 8,
        "y": 4,
        "z": 10,
    }
    word_total = 0
    for letter in user_input:
        word_total += score[letter]
    return word_total


if __name__ == "__main__":
    main()
