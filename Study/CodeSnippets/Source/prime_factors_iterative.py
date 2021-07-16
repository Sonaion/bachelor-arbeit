def helper(number):
    if number == 1:
        return False
    for check_num in range(2, int(number / 2) + 1):
        if number % check_num == 0:
            return False
    return True


def function(number):
    result = []
    for idx_num in range(2, number + 1):
        if helper(idx_num) and number % idx_num == 0:
            result.append(idx_num)
    return result


print(function(18))
