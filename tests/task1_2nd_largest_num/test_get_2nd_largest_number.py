import pytest

from task2_2nd_largest_num import get_2nd_largest


def test_when_given_parameter_is_less_than_2():
    with pytest.raises(IndexError):
        get_2nd_largest([1])


def test_get_number():
    actual = get_2nd_largest([1, 2, 3, 4, 5])

    assert actual == 4
