def helper(number):
    return len([value for value in range(1, number + 1) if number % value == 0]) == 2


def function(number):
    return [x for x in range(2, number + 1) if helper(x) and number % x == 0]


print(function(18))
