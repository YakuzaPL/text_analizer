import pytest
from words_counter import words_counter


def test_words_counter():
    assert words_counter("Lorem ipsum dolor sit amet.") in {"lorem": 1,
                                                            "ipsum": 1,
                                                            "dolor": 1,
                                                            "sit": 1,
                                                            "amet": 1
                                                            }