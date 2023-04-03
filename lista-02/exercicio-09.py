def operate_matrix_lines(matrix, operator):
    """Operates on a matrix element(line) using the map function
    with a function called operator passed as argument"""
    return list(map(operator, matrix))


def sum_line(line):
    """Returns the sum of a list"""
    return sum(line)


A = [[0, 2, 3], [4, 5, 6], [7, -1, 19]]
for sums in operate_matrix_lines(A, sum_line):
    print(sums)

B = print(operate_matrix_lines(A, sum_line))
print(B)
