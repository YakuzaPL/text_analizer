import pytest
from file_receiv import open_txt_file


def test_open_txt_file():
    assert open_txt_file("test_file_txt") == "this is the test file for txt"

