def function(number):
    if number == 1:
        return False
    for check_num in range(2, int(number / 2) + 1):
        if number % check_num == 0:
            return False
    return True


print(function(7))
