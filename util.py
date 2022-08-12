import os
from math import ceil
from random import shuffle


def clear_terminal() -> None:
    """Clears the program's terminal."""

    os.system('cls' if os.name == 'nt' else 'clear')


def split_array(array: tuple | list, parts: int = 2, shuffle_division_map: bool = False) -> tuple:
    """Splits a tuple or a list into a given count of parts packed in tuple.

    :param array: an array (tuple | list) for splitting.

    :param parts: a count of parts we want to split the array
                  (parts count must be higher than 0 and lower than the array length). Default value: 2 parts.

    :param shuffle_division_map: if it's impossible to divide the array into parts with equal length, shuffle
                                 the division map so random parts will store more elements than others, no matter
                                 the parts order. Default value: False.

    :returns: tuple of separated array's parts (tuples or lists, depends on what array type was used).

    :raises ValueError: if parts count is lower than 0 or higher than the array length."""

    if parts < 1:
        raise ValueError('Parts count must be higher than 0.')
    length = len(array)
    if length < parts:
        raise ValueError('Parts count is higher than the array length.')

    unfinished_array_length = len(array)
    division_map = []

    for i in range(parts):
        elements_count = ceil(unfinished_array_length / (parts - i))
        array_division_remainder = unfinished_array_length % (parts - i)
        division_map.append(elements_count if elements_count <= unfinished_array_length else array_division_remainder)
        unfinished_array_length -= elements_count

    if shuffle_division_map and length % parts:
        shuffle(division_map)

    result = []
    for map_step, elements_count in enumerate(division_map):
        slice_start_index = sum(division_map[:map_step])
        slice_end_index = sum(division_map[:map_step]) + elements_count
        result.append(array[slice_start_index:slice_end_index])

    return tuple(result)
