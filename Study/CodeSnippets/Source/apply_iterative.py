def function(array_data, func):
    results = []
    for data in array_data:
        results.append(func(data))
    return results


print(function([1, 2, 3], lambda x: x ** 2 + x))
