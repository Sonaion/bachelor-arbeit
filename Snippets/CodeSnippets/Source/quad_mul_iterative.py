def function(n):
    array_data = []
    for i in range(1, n + 1):
        array_data.append(i ** 2)
    result = 1
    for value in array_data:
        result *= value
    return result
