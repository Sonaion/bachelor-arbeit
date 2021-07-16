def helper(number):
    number_array = range(1, number + 1)
    prime_array = filter(lambda x: number % x == 0, number_array)
    return len(list(prime_array)) == 2


def function(number):
    primes = filter(helper, range(2, number + 1))
    prime_factors = filter(lambda x: number % x == 0, primes)
    return list(prime_factors)


print(function(18))
