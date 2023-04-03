def multiply_matrices(A, B):
    """Multiplies two matrices and returns the resultant matrix,
    returns false if the operation is
    not allowed"""
    m = len(A)
    hA = len(A[0])
    n = len(B[0])
    hB = len(B)

    if hA != hB:
        return False
    else:
        h = hA = hB

    C = [[0] * n for i in range(m)]
    for i in range(m):
        for j in range(n):
            for k in range(h):
                C[i][j] += A[i][k] * B[k][j]
    return C


A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
A = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
B = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(multiply_matrices(A, B))
