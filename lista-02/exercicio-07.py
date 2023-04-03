import math


def is_prime(num):
    for k in range(2, num):
        if num % k == 0:
            return False
    return True


def get_primes():
    num = 2
    while True:
        # if num == 2:
        #     yield num
        if is_prime(num):
            yield num
        num += 1


for i in get_primes():
    if i > 100:
        break
    print(i, end=" ")
