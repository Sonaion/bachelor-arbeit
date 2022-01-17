from functools import reduce


def function(n):
    array_data = [value for value in range(2, n + 1) if value % 3 == 0 or value % 4 == 0]
    total = 0
    scanned = [total := total + x for x in array_data]
    return scanned[-1]


print(function(14))
