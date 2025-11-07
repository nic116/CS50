import pytest
from twttr import shorten


def test_shorten_lower():
    assert shorten("hello world") == "hll wrld"
    
def test_shorten_upper():
    assert shorten("HELLO") == "HLL"
    
def test_shorten_punctuation():
    assert shorten(",./!_?") == ",./!_?"
    
def test_shorten_novowel():
    assert shorten("Hll wrld") == "Hll wrld"

def test_shorten_numbers():
    assert shorten("1234567890") == "1234567890"

def test_shorten_empty():
    assert shorten("") == ""