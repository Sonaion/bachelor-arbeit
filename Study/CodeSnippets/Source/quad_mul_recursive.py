def function(n):
    if n == 1:
        return 1
    return n ** 2 * function(n - 1)


print(function(3))
