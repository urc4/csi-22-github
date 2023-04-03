def operate_matrix_lines(matrix, operator):
    return list(map(operator, matrix))


def sum_line(line):
    return sum(line)


A = [[1, 2, 3], [4, 5, 6], [7, -1, 19]]
for sums in operate_matrix_lines(A, sum_line):
    print(sums)

B = print(operate_matrix_lines(A, sum_line))
print(B)
