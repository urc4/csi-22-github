import math


def get_primes():
    num = 3
    while True:
        for k in range(2, num):
            if num % k == 0:
                num = num + 1
                break
        yield num
        num = num + 1


for i in get_primes():
    if i > 100:
        break
    print(i, end=" ")
