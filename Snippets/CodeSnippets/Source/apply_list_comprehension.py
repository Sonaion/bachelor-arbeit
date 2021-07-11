def function(array_data, func):
    return [func(data) for data in array_data]


print(function([1, 2, 3], lambda x: x ** 2 + x))
