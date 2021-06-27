def function(array_data, func):
    return list(map(func, array_data))


print(function([1, 2, 3], lambda x: x ** 2 + x))
