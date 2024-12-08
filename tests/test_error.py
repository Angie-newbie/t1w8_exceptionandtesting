import pytest
from src.error import convert_to_interger


def test_integer():
    assert convert_to_interger('123') == 123

def test_string():
    assert convert_to_interger('123') == 123

def test_float():
    convert_to_interger('123.45')