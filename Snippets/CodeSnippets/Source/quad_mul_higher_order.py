def function(n):
    array_data = map(lambda x: x ** 2, range(1, n + 1))
    return reduce(lambda x, y: x * y, array_data)
