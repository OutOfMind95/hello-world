from working import convert
import pytest


def test_ValueError():
    with pytest.raises(ValueError):
        convert("13:00 AM to 5:00 PM")


def test_minutes():
    assert convert("9:30 AM to 5:45 PM") == "09:30 to 17:45"


def test_format():
    with pytest.raises(ValueError):
        convert("9-00 AM to 5-00 PM")


def test_convert():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"


def test_range():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:00 PM")


def test_mid():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"


def test_to():
    with pytest.raises(ValueError):
        convert("9 AM 5 AM")
