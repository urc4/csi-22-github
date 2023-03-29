def get_inner_product(u, v):
    if len(u) != len(v):
        return False
    dimension = len(u)
    in_p = 0
    for index in range(dimension):
        in_p += u[index] * v[index]
    return in_p


def multiply_matrices(A, B):
    """Multiplies two matrices"""
    m_dim = len(B)
    for i in range(m_dim):
        m_elem = 0
    pass


A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

u = A[0]
v = A[1]
print(len(A))
print(get_inner_product(u, v))
