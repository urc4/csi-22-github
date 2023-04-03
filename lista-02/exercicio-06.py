def gen_inv_list(_list):
    index = len(_list) - 1
    while index >= 0:
        yield _list[index]
        index = index - 1


_list = [4, 7, 8]

for value in gen_inv_list(_list):
    print(value)

values = gen_inv_list(_list)

print(list(values))

# print(next(values))
# print(next(values))
# print(next(values))
