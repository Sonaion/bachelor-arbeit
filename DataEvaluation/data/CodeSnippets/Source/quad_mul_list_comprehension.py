from functools import reduce


def function(n):
    array_data = [x**2 for x in range(1, n + 1)]
    total = 1
    scanned = [total := total * x for x in array_data]
    return scanned[-1]


print(function(3))
