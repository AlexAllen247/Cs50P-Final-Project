from project import random_letters, check_word, word_score


def main():
    test_random_letters()
    test_check_word()
    test_word_score()


def test_random_letters():
    assert random_letters() == random_letters()


def test_check_word():
    assert check_word("axe") == "axe"
    assert check_word("zoo") == "zoo"
    assert check_word("tooth") != "booth"


def test_word_score():
    assert word_score("axe") == 10
    assert word_score("zoo") == 12
    assert word_score("hoot") == 7


if __name__ == "__main__":
    main()
