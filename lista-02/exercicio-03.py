def filter_decimal_alphabet(l_strings):
    """Filters strings that contain alphabetic and decimal characters"""
    alnum_strings = []
    for str in l_strings:
        if str.isalnum():
            alnum_strings.append(str)

    return alnum_strings


def filter_decimal_alphabet_filter(l_strings):
    """Filters strings that contain alphabetic and decimal characters"""

    return list(filter(lambda str: str.isalnum() == 1, l_strings))


l_strings = [
    "oi",
    "plameiras",
    ".tr45",
    "..;;;;fas",
    "45gfd6gfd",
    "45546465",
    "'a;sd';@",
    "re3@",
    "",
    "ultimo",
]


print(filter_decimal_alphabet(l_strings))
print(filter_decimal_alphabet_filter(l_strings))
