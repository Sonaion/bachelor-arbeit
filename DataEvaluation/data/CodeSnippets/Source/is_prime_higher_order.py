def function(number):
    number_array = range(1, number + 1)
    prime_array = filter(lambda x: number % x == 0, number_array)
    return len(list(prime_array)) == 2


print(function(7))
