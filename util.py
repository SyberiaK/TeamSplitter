import os
from math import ceil
from random import shuffle


def clear_terminal() -> None:
    """Clears the program's terminal."""

    os.system('cls' if os.name == 'nt' else 'clear')


def split_array(arr: tuple | list, parts: int = 2, shuffle_division: bool = False) -> tuple:
    """Splits a tuple or a list into a given count of parts packed in tuple.

    :param arr: an array (tuple | list) for splitting.

    :param parts: a count of parts we want to split the array
                  (parts count must be higher than 0 and lower than the array length).

    :param shuffle_division: if it's impossible to divide the array into parts with equal length,
                             random parts will store more elements than others, no matter the parts order.

    :returns: tuple of separated array's parts (lists).

    :raises ValueError: if parts count is lower than 0 or higher than the array length."""

    if parts < 1:
        raise ValueError('Parts count must be higher than 0.')
    length = len(arr)
    if length < parts:
        raise ValueError('Parts count is higher than the array length.')

    arr, divs = list(arr), []
    for i in range(parts):
        count = ceil(length / (parts - i))
        divs.append(count if count <= length else length % (parts - i))
        length -= count

    shuffle(divs) if shuffle_division and len(arr) % parts else None

    return tuple(arr[sum(divs[:i]):sum(divs[:i]) + v] for i, v in enumerate(divs))
