def function(n):
    if n == 1:
        return 0
    if n % 3 == 0 or n % 4 == 0:
        return n + function(n - 1)
    else:
        return function(n - 1)
