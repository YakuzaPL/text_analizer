import pytest
from words_counter import text_to_words, letters_dict_creator, text_to_letters


def text_to_words():
    assert text_to_words("Some example text, given here.") == ['Some', 'example', 'text', 'given', 'here']


def test_text_to_letters():
    sentence = "Hello World!"
    assert text_to_letters(sentence) == ['H', 'e', "l", 'l', 'o', 'W', 'o', 'r', 'l', 'd']


def test_words_or_letters_counter():
    list_of_words = ['Some', 'some', 'exaple', 'teXt', 'given', 'Here', 'just', 'for', 'fun']
    list_od_letters = ['H', 'e', "l", 'l', 'o', 'W', 'o', 'r', 'l', 'd']
    assert letters_dict_creator(list_of_words) == {'some': 2, 'exaple': 1, 'text': 1, 'given': 1, 'here': 1,
                                                            'just': 1,
                                                            'for': 1, 'fun': 1}

    assert letters_dict_creator(list_od_letters) == {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}
