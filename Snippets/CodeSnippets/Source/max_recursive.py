def function(array_data, current=None):
    if len(array_data) == 0:
        return current
    elif current is None:
        return function(array_data[1:], array_data[0])
    elif current >= array_data[0]:
        return function(array_data[1:], current)
    else:
        return function(array_data[1:], array_data[0])
