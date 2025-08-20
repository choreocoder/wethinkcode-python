import pytest

from twttr import shorten

def test_shorten_basic():
    # basic examples
    assert shorten("twitter") == "twttr"
    assert shorten("Twitter") == "Twttr"
    assert shorten("hello world") == "hll wrld"

def test_returns_str():
    result = shorten("test")
    assert isinstance(result, str)

def test_edge_cases():
    assert shorten("") == ""           # empty string
    assert shorten("aeiouAEIOU") == "" # all vowels
    assert shorten("CS50") == "CS50"   # digits
    assert shorten("sky") == "sky"     # no vowels
    assert shorten ("hello, world!") == "hll, wrld!" #punctuation


