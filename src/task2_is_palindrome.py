""" Solution for task2 """


def is_palindrome(value: str) -> bool:
    if value == value[::-1]:
        return True
    return False
