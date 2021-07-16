def function(number, current=None):
    if current is None:
        current = int(number / 2)
    if number == 1:
        return False
    if current == 1:
        return True
    if number % current == 0:
        return False
    return function(number, current - 1)


print(function(7))
