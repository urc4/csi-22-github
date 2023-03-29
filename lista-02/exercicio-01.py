def remove_empty_tuples(_tuple):
    """Removes empty tuples"""
    _list = list(_tuple)
    empty_indexes = []

    for index, tup in enumerate(_list):
        if len(tup) == 0:
            empty_indexes.append(index)

    fix_index = 0

    for index in empty_indexes:
        _list.pop(index - fix_index)
        fix_index += 1

    return tuple(_list)


# poderia fazer while () is in ... remove

_tuple = (
    (),
    (3, 2),
    (2, 1, 4, 5),
    (),
    (),
    (3, 4, 5, 6, 7, 8, 9, 10, 1),
    (),
    (),
    (),
    (),
    (),
    (),
    (),
    (),
    (),
    (2, 1),
)
# does python pass by reference
new_tuple = remove_empty_tuples(_tuple)
print(_tuple)
print(new_tuple)
