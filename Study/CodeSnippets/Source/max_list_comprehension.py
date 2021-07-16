from functools import reduce


def function(array_data):
    max_value = array_data[0]
    scanned = [max_value := x for x in array_data if x > max_value]
    return scanned[-1]


print(function([0, 5, 2]))
