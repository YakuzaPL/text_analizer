import pytest
from words_counter import text_splitter, words_counter

def test_text_splitter():
    assert text_splitter("Some example text, given here.") == ['Some', 'example', 'text', 'given', 'here']


def test_words_counter():
    list_of_words = ['Some', 'some', 'exaple', 'teXt', 'given', 'Here', 'just', 'for', 'fun']
    assert words_counter(list_of_words) == {'some': 2, 'exaple': 1, 'text': 1, 'given': 1, 'here': 1, 'just': 1,
                                            'for': 1, 'fun': 1}