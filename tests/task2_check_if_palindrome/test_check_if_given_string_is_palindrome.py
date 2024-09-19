import pytest


def is_palindrome(value: str) -> bool:
    pass


@pytest.mark.parametrize('tc_input, expect', [('asd', False), ('ada', True)])
def test_if_string_is_palindrome(tc_input, expect):
    actual = is_palindrome(tc_input)

    assert actual == expect
