def function(data_array, element):
    for idx, value in enumerate(data_array):
        if value == element:
            return idx
    return -1
