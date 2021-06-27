def function(array_data, func):
    results = []
    for data in array_data:
        results.append(func(data))
    return results
