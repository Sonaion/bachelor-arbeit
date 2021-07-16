def function(array_data):
    if len(array_data) == 0:
        return None

    max_value = array_data[0]
    for value in array_data:
        if value > max_value:
            max_value = value
    return max_value


print(function([0, 5, 2]))
