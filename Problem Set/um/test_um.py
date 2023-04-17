from um import count


def test_capitalize():
    assert count("Um UM um") == 3


def test_punctuation():
    assert count("um...") == 1


def test_inword():
    assert count("yummy") == 0


def test_zero():
    assert count("hello, world") == 0