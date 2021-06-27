def function(array_data):
    if len(array_data) == 0:
        return []
    return [array_data[0] + 5] + function(array_data[1:])
