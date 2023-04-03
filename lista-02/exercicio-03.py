def filter_alphanum(strings_list):
    """Filters strings that contain alphabetic and decimal characters from a list of strings"""

    return list(
        filter(
            lambda str: any(char.isdigit() or char.isalpha() for char in str),
            strings_list,
        )
    )


strings_list = [
    "oi",
    "plameiras",
    ".tr45",
    "..;;;;fas",
    "45gfd6gfd",
    "45546465",
    "'a;sd';@",
    "re3@",
    "",
    ".............",
    "ultimo",
]

print(strings_list)
print(filter_alphanum(strings_list))
