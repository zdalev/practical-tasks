"""Solution for task 1"""


def get_2nd_largest(values: list[int]) -> int:
    if len(values) < 2:
        raise IndexError('Given list length is less than 2.')

    _values = set(values)  # to remove duplicates

    sort = sorted(values, reverse=True)
    result = sort[1]

    return result
