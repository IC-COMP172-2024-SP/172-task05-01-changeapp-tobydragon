import pytest
from change_library import count_change, make_change_cents, make_change_dollars, convert_str_to_int, convert_str_to_float


def test_count_change():
    assert count_change(1, 1, 1, 1) == pytest.approx(0.41)
    assert count_change(0, 2, 0, 2) == pytest.approx(0.6)
    assert count_change(0, 0, 0, 0) == pytest.approx(0)
    assert count_change(3, 12, 7, 9) == pytest.approx(3.58)
    assert count_change(99, 111, 200, 100) == pytest.approx(51.54)


def test_convert_str_to_int():
    assert convert_str_to_int("1") == 1
    assert convert_str_to_int("3456") == 3456
    assert convert_str_to_int("3.5") == 0
    assert convert_str_to_int("0") == 0
    assert convert_str_to_int("hello") == 0
    assert convert_str_to_int("") == 0


def test_make_change_cents():
    assert make_change_cents(41) == [1, 1, 1, 1]
    assert make_change_cents(60) == [0, 0, 1, 2]
    assert make_change_cents(45) == [0, 0, 2, 1]
    assert make_change_cents(121) == [1, 0, 2, 4]
    assert make_change_cents(9) == [4, 1, 0, 0]
    assert make_change_cents(5158) == [3, 1, 0, 206]
    assert make_change_cents(0) == [0, 0, 0, 0]
    with pytest.raises(ValueError):
        make_change_cents(1.1)


def test_make_change_dollars():
    assert make_change_dollars(0.41) == [1, 1, 1, 1, 0]
    assert make_change_dollars(1.41) == [1, 1, 1, 1, 1]
    assert make_change_dollars(51.58) == [3, 1, 0, 2, 51]
    assert make_change_dollars(0) == [0, 0, 0, 0, 0]
    assert make_change_dollars(0.26) == [1, 0, 0, 1, 0]
    assert make_change_dollars(0.25) == [0, 0, 0, 1, 0]
    assert make_change_dollars(0.1) == [0, 0, 1, 0, 0]
    assert make_change_dollars(0.05) == [0, 1, 0, 0, 0]
    assert make_change_dollars(0.01) == [1, 0, 0, 0, 0]
    assert make_change_dollars(0.00999) == [0, 0, 0, 0, 0]


def test_convert_str_to_float():
    assert convert_str_to_float("1") == pytest.approx(1.0)
    assert convert_str_to_float("1.1") == pytest.approx(1.1)
    assert convert_str_to_float("2.3456") == pytest.approx(2.3456)
    assert convert_str_to_float("0") == pytest.approx(0.0)
    assert convert_str_to_float("0.0") == pytest.approx(0.0)
    assert convert_str_to_float("anything") == pytest.approx(0.0)
    assert convert_str_to_float("") == pytest.approx(0.0)


