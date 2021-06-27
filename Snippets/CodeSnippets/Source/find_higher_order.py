def function(data_array, element):
    index_data_array = enumerate(data_array)
    filtered_array = map(lambda x_tuple: x_tuple[0] if x_tuple[1] == element else 0, index_data_array)
    return reduce(lambda x, y: x + y, filtered_array)
