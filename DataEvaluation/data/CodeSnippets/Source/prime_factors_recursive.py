def helper(number, current=None):
    if current is None:
        current = int(number / 2)
    if number == 1:
        return False
    if current == 1:
        return True
    if number % current == 0:
        return False
    return helper(number, current - 1)


def function(number, current=None):
    if current is None:
        return function(number, 2)

    elif number == current and number % current == 0:
        return [current]

    elif number <= current:
        return []

    elif not helper(current):
        return function(number, current + 1)

    elif number % current == 0:
        return [current] + function(number / current, current + 1)

    else:
        return function(number, current + 1)


print(function(18))
