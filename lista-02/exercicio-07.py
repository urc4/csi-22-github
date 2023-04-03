def is_prime(num):
    """Checks if a number num is prime"""
    for k in range(2, num):
        if num % k == 0:
            return False
    return True


def get_primes():
    """Generates an infinite list of prime numbers"""
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1


for i in get_primes():
    if i > 2000:
        break
    print(i, end=" ")
