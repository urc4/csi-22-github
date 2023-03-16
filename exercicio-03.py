# def sum_to(n):
#     """Find the sum of all integres up to and including n by iterative means"""
#     sum = 0
#     for k in range(n+1):
#         sum = sum + k
#     return sum


def sum_to(n):
   """Find the sum of all integres up to and including n by mathematical means"""
   return n*(n+1)/2


print(int(sum_to(10)))
