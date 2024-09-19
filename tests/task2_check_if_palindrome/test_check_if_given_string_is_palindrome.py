import pytest

from task2_is_palindrome import is_palindrome


@pytest.mark.parametrize('tc_input, expect', [('asd', False), ('ada', True), ('saippuakivikauppias', True)])
def test_if_string_is_palindrome(tc_input, expect):
    actual = is_palindrome(tc_input)

    assert actual == expect
