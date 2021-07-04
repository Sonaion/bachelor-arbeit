########################################################################################################################
#add_5_higher_order

def function(array_data):
    return list(map(lambda x: x + 5, array_data))


print(function([0, 5, 10]))



########################################################################################################################
#add_5_iterative

def function(array_data):
    result = []
    for element in array_data:
        result.append(element + 5)
    return result


print(function([0, 5, 10]))



########################################################################################################################
#add_5_recursive

def function(array_data):
    if len(array_data) == 0:
        return []
    return [array_data[0] + 5] + function(array_data[1:])


print(function([0, 5, 10]))



########################################################################################################################
#apply_higher_order

def function(array_data, func):
    return list(map(func, array_data))


print(function([1, 2, 3], lambda x: x ** 2 + x))



########################################################################################################################
#apply_iterative

def function(array_data, func):
    results = []
    for data in array_data:
        results.append(func(data))
    return results


print(function([1, 2, 3], lambda x: x ** 2 + x))



########################################################################################################################
#apply_recursive

def function(array_data, func):
    if len(array_data) == 0:
        return []
    else:
        return [func(array_data[0])] + function(array_data[1:], func)


print(function([1, 2, 3], lambda x: x ** 2 + x))



########################################################################################################################
#condition_sum_higher_order

def function(n):
    array_data = filter(lambda x: x % 3 == 0 or x % 4 == 0, range(2, n + 1))
    return reduce(lambda x, y: x + y, array_data)


print(function(14))



########################################################################################################################
#condition_sum_iterative

def function(n):
    array_data = []
    for i in range(2, n + 1):
        if i % 3 == 0 or i % 4 == 0:
            array_data.append(i)
    result = 0
    for value in array_data:
        result += value
    return result


print(function(14))



########################################################################################################################
#condition_sum_recursive

def function(n):
    if n == 1:
        return 0
    if n % 3 == 0 or n % 4 == 0:
        return n + function(n - 1)
    else:
        return function(n - 1)


print(function(14))



########################################################################################################################
#find_higher_order

def function(data_array, element):
    index_data_array = enumerate(data_array)
    filtered_array = map(lambda x_tuple: x_tuple[0] if x_tuple[1] == element else 0, index_data_array)
    return reduce(lambda x, y: x + y, filtered_array)


print(function([1, 2, 3, 4, 5], 3))



########################################################################################################################
#find_iterative

def function(data_array, element):
    for idx, value in enumerate(data_array):
        if value == element:
            return idx
    return -1


print(function([1, 2, 3, 4, 5], 3))



########################################################################################################################
#find_recursive

def function(data_array, element):
    if len(data_array) == 0:
        return -1
    elif data_array[0] == element:
        return 0
    else:
        idx = function(data_array[1:], element)
        if idx == -1:
            return -1
        else:
            return idx + 1


print(function([1, 2, 3, 4, 5], 3))



########################################################################################################################
#is_prime_higher_order

def function(number):
    number_array = range(1, number + 1)
    prime_array = filter(lambda x: number % x == 0, number_array)
    return len(list(prime_array)) == 2


print(function(7))



########################################################################################################################
#is_prime_iterative

def function(number):
    if number == 1:
        return False
    for check_num in range(2, int(number / 2) + 1):
        if number % check_num == 0:
            return False
    return True


print(function(7))



########################################################################################################################
#is_prime_recursive

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



########################################################################################################################
#max_higher_order

def function(array_data):
    return reduce(lambda x, y: x if x >= y else y, array_data)


print(function([0, 5, 2]))



########################################################################################################################
#max_iterative

def function(array_data):
    if len(array_data) == 0:
        return None

    max_value = array_data[0]
    for value in array_data:
        if value > max_value:
            max_value = value
    return max_value


print(function([0, 5, 2]))



########################################################################################################################
#max_recursive

def function(array_data, current=None):
    if len(array_data) == 0:
        return current
    elif current is None:
        return function(array_data[1:], array_data[0])
    elif current >= array_data[0]:
        return function(array_data[1:], current)
    else:
        return function(array_data[1:], array_data[0])


print(function([0, 5, 2]))



########################################################################################################################
#node_higher_order

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def pre_order_iter(self):
        result = [self]
        if self.left is not None:
            left = self.left.pre_order_iter()
            result = result + left
        if self.right is not None:
            right = self.right.pre_order_iter()
            result = result + right
        return result


def function(node):
    duos = product(node.pre_order_iter(), node.pre_order_iter())
    multiplies = map(lambda x: x[0].value * x[1].value, duos)
    return reduce(lambda x, y: x + y, multiplies)


n = Node(2)
n.left = Node(1)
n.right = Node(3)
print(function(n))



########################################################################################################################
#node_iterative

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def pre_order_iter(self):
        stack = []
        result = []
        stack.append(self)

        while len(stack) != 0:
            node = stack.pop()
            result.append(node)

            if node.right is not None:
                stack.append(node.right)

            if node.left is not None:
                stack.append(node.left)

        return result


def function(node):
    result = 0
    for current1 in node.pre_order_iter():
        for current2 in node.pre_order_iter():
            result += current1.value * current2.value
    return result


n = Node(2)
n.left = Node(1)
n.right = Node(3)
print(function(n))



########################################################################################################################
#node_recursive

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def pre_order_iter(self):
        result = []
        result.append(self)
        if self.left is not None:
            left = self.left.pre_order_iter()
            result = result + left
        if self.right is not None:
            right = self.right.pre_order_iter()
            result = result + right
        return result


def helper(first, second, second_len=None):
    if len(first) == 0:
        return []

    if len(second) == 0:
        return []

    if second_len is None:
        return helper(first, second, len(second))

    result = [(first[0], second[0])]
    if len(second) == second_len:
        inner = helper(first, second[1:], second_len)
        outer = helper(first[1:], second, second_len)
        result = result + inner + outer
    else:
        inner = helper(first, second[1:], second_len)
        result = result + inner
    return result


def function(powerset):
    if len(powerset) == 0:
        return 0
    return powerset[0][0].value * powerset[0][1].value + function(powerset[1:])


n = Node(2)
n.left = Node(1)
n.right = Node(3)
print(function(helper(n.pre_order_iter(), n.pre_order_iter())))



########################################################################################################################
#prime_factors_higher_order

def helper(number):
    number_array = range(1, number + 1)
    prime_array = filter(lambda x: number % x == 0, number_array)
    return len(list(prime_array)) == 2


def function(number):
    primes = filter(helper, range(2, number + 1))
    prime_factors = filter(lambda x: number % x == 0, primes)
    return list(prime_factors)


print(function(18))



########################################################################################################################
#prime_factors_iterative

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



########################################################################################################################
#prime_factors_recursive

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



########################################################################################################################
#quad_mul_higher_order

def function(n):
    array_data = map(lambda x: x ** 2, range(1, n + 1))
    return reduce(lambda x, y: x * y, array_data)


print(function(3))



########################################################################################################################
#quad_mul_iterative

def function(n):
    array_data = []
    for i in range(1, n + 1):
        array_data.append(i ** 2)
    result = 1
    for value in array_data:
        result *= value
    return result


print(function(3))



########################################################################################################################
#quad_mul_recursive

def function(n):
    if n == 1:
        return 1
    return n ** 2 * function(n - 1)


print(function(3))



########################################################################################################################
#students_higher_order

class Student:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def __repr__(self):
        return str(self.name)


def function(student_array):
    return list(filter(lambda x: x.age >= 18, student_array))


students = []
students.append(Student(17, "Hans"))
students.append(Student(21, "Jasmin"))
students.append(Student(32, "Florian"))
print(function(students))



########################################################################################################################
#students_iterative

class Student:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def __repr__(self):
        return str(self.name)


def function(student_array):
    result = []
    for student in student_array:
        if student.age >= 18:
            result.append(student)
    return result


students = []
students.append(Student(17, "Hans"))
students.append(Student(21, "Jasmin"))
students.append(Student(32, "Florian"))
print(function(students))



########################################################################################################################
#students_recursive

class Student:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def __repr__(self):
        return str(self.name)


def function(student_array):
    if len(student_array) == 0:
        return []
    elif student_array[0].age >= 18:
        return [student_array[0]] + function(student_array[1:])
    else:
        return function(student_array[1:])


students = []
students.append(Student(17, "Hans"))
students.append(Student(21, "Jasmin"))
students.append(Student(32, "Florian"))
print(function(students))



