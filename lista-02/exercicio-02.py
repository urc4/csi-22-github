def get_averages(tuples):
    """Returns the average by 2"""
    averages = []
    for tup in tuples:
        sum = 0
        for num in tup:
            sum += num
        averages.append(sum / 2)
    return tuple(averages)


tuples = ((2, 3, 4), (3, 4, 5, 6), (2, 4), (4, 8, 9))
print(get_averages(tuples))
