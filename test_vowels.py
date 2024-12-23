import pytest
from main import count_vowels

def test_all_vowels():
    assert count_vowels("аеёиоуыэюяАЕЁИОУЫЭЮЯ") == 20

def test_no_vowels():
    assert count_vowels("бвгджзйклмнпрстфхцчшщ") == 0

def test_mixed_string():
    assert count_vowels("Привет, мир!") == 3

def test_empty_string():
    assert count_vowels("") == 0

def test_numbers_and_special_characters():
    assert count_vowels("1234!@#$%^&*()") == 0