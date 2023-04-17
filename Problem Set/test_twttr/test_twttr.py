from twttr import shorten

def test_shorten():
    assert shorten("This is a test") == "Ths s  tst"

def test_upper():
    assert shorten("THIS IS A TEST") == "THS S  TST"

def test_punctuation():
    assert shorten("IS THIS A TEST??!?") == "S THS  TST??!?"

def test_number():
    assert shorten("1 TEST") == "1 TST"