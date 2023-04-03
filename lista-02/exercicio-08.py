def filter_even(numbers):
    """Filters even numbers in a list of numbers"""
    return list(filter(lambda num: num % 2 == 0, numbers))


numbers = [4, 7, 87, 45, 34, 6, 88, 23, 556, 8745, 2345, 56]
for even in filter_even(numbers):
    print(even)
