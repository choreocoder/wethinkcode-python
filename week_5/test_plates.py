import plates

def test_valid_length():
    assert plates.is_valid("CS")      # minimum length
    assert plates.is_valid("CS50")    # valid middle
    assert not plates.is_valid("C")   # too short
    assert not plates.is_valid("CS50AA")  # too long

def test_starts_with_two_letters():
    assert plates.is_valid("CS50")
    assert not plates.is_valid("1CS50")
    assert not plates.is_valid("C5")

def test_numbers_only_at_end():
    assert plates.is_valid("CS50")
    assert not plates.is_valid("CS50P")   # letter after number
    assert not plates.is_valid("CS05")    # leading zero in numbers

def test_has_only_alphanumerics():
    assert plates.is_valid("HELLO")
    assert not plates.is_valid("HELLO!")  # contains punctuation
    assert not plates.is_valid("HI HI")   # contains space