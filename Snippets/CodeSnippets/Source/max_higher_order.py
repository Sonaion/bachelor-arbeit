def function(array_data):
    return reduce(lambda x, y: x if x >= y else y, array_data)
