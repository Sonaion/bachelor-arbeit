from functools import reduce


def function(data_array, element):
    return [idx for (idx, value) in enumerate(data_array) if value == element][0]


print(function([1, 2, 3, 4, 5], 3))
