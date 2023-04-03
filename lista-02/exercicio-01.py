def remove_all_empty_tuples(tuples):
    """Removes all empty tuples from a list of empty tuples"""
    empty_tup = ()
    while empty_tup in tuples:
        tuples.remove(empty_tup)
    return tuple(tuples)


tuples = (
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
print(tuples)
print(() in tuples)
tuples = remove_all_empty_tuples(list(tuples))
print(tuples)
print(() in tuples)
