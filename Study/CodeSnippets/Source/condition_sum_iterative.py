def function(n):
    array_data = []
    for i in range(2, n + 1):
        if i % 3 == 0 or i % 4 == 0:
            array_data.append(i)
    result = 0
    for value in array_data:
        result += value
    return result


print(function(14))
