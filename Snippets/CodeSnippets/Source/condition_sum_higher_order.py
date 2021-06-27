def function(n):
    array_data = filter(lambda x: x % 3 == 0 or x % 4 == 0, range(2, n + 1))
    return reduce(lambda x, y: x + y, array_data)
