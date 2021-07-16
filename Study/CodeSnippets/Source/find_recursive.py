def function(data_array, element):
    if len(data_array) == 0:
        return -1
    elif data_array[0] == element:
        return 0
    else:
        idx = function(data_array[1:], element)
        if idx == -1:
            return -1
        else:
            return idx + 1


print(function([1, 2, 3, 4, 5], 3))
