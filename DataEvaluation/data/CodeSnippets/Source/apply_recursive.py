def function(array_data, func):
    if len(array_data) == 0:
        return []
    else:
        return [func(array_data[0])] + function(array_data[1:], func)


print(function([1, 2, 3], lambda x: x ** 2 + x))
