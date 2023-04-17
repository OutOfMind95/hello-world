from numb3rs import validate


def test_outofrange():
    assert validate("275.2.2.2") == False


def test_outofrange2():
    assert validate("2.275.2.2") == False


def test_outofrange3():
    assert validate("2.2.275.2") == False


def test_outofrange4():
    assert validate("2.2.2.275") == False


def test_str():
    assert validate("cat") == False


def test_notanip():
    assert validate("2.2.2.2.2") == False
