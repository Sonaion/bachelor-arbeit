def function(number):
    return len([value for value in range(1, number+1) if number % value == 0]) == 2


print(function(7))
