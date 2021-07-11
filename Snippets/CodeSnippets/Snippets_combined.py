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
#add_5_list_comprehension

def function(array_data):
    return [data + 5 for data in array_data]


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
#apply_list_comprehension

def function(array_data, func):
    return [func(data) for data in array_data]


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
#Computer_higher_order

class Computer:
    id = 0

    def __init__(self, cpu, gpu, ram):
        self.cpu = cpu
        self.gpu = gpu
        self.ram = ram
        self.id = Computer.id
        Computer.id += 1

    def __repr__(self):
        return str(self.id)


def function(computer_array):
    return list(filter(lambda x: "AMD" in x.cpu and "NVIDIA GTX30" in x.gpu and x.ram >= 16, computer_array))


computer_array = []
computer_array.append(Computer("INTEL i7-860", "NVIDIA GTX3080", 16))
computer_array.append(Computer("AMD 5900x", "NVIDIA GTX3080", 32))
computer_array.append(Computer("INTEL i9-10900T", "NVIDIA GTX1070", 8))
computer_array.append(Computer("AMD 5900x", "AMD RX6900", 8))
computer_array.append(Computer("AMD 5700", "AMD RX6900", 16))
computer_array.append(Computer("AMD 5900x", "NVIDIA GTX3090", 64))
computer_array.append(Computer("INTEL i5-8400", "NVIDIA GTX1060", 4))
print(function(computer_array))



########################################################################################################################
#Computer_iterative

class Computer:
    id = 0

    def __init__(self, cpu, gpu, ram):
        self.cpu = cpu
        self.gpu = gpu
        self.ram = ram
        self.id = Computer.id
        Computer.id += 1

    def __repr__(self):
        return str(self.id)


def function(computer_array):
    results = []
    for computer in computer_array:
        if "AMD" in computer.cpu and "NVIDIA GTX30" in computer.gpu and computer.ram >= 16:
            results.append(computer)
    return results


computer_array = []
computer_array.append(Computer("INTEL i7-860", "NVIDIA GTX3080", 16))
computer_array.append(Computer("AMD 5900x", "NVIDIA GTX3080", 32))
computer_array.append(Computer("INTEL i9-10900T", "NVIDIA GTX1070", 8))
computer_array.append(Computer("AMD 5900x", "AMD RX6900", 8))
computer_array.append(Computer("AMD 5700", "AMD RX6900", 16))
computer_array.append(Computer("AMD 5900x", "NVIDIA GTX3090", 64))
computer_array.append(Computer("INTEL i5-8400", "NVIDIA GTX1060", 4))
print(function(computer_array))



########################################################################################################################
#Computer_list_comprehension

class Computer:
    id = 0

    def __init__(self, cpu, gpu, ram):
        self.cpu = cpu
        self.gpu = gpu
        self.ram = ram
        self.id = Computer.id
        Computer.id += 1

    def __repr__(self):
        return str(self.id)


def function(computer_array):
    return [computer for computer in computer_array if "AMD" in computer.cpu and "NVIDIA GTX30" in computer.gpu and computer.ram >= 16]


computer_array = []
computer_array.append(Computer("INTEL i7-860", "NVIDIA GTX3080", 16))
computer_array.append(Computer("AMD 5900x", "NVIDIA GTX3080", 32))
computer_array.append(Computer("INTEL i9-10900T", "NVIDIA GTX1070", 8))
computer_array.append(Computer("AMD 5900x", "AMD RX6900", 8))
computer_array.append(Computer("AMD 5700", "AMD RX6900", 16))
computer_array.append(Computer("AMD 5900x", "NVIDIA GTX3090", 64))
computer_array.append(Computer("INTEL i5-8400", "NVIDIA GTX1060", 4))
print(function(computer_array))



########################################################################################################################
#Computer_recursive

class Computer:
    id = 0

    def __init__(self, cpu, gpu, ram):
        self.cpu = cpu
        self.gpu = gpu
        self.ram = ram
        self.id = Computer.id
        Computer.id += 1

    def __repr__(self):
        return str(self.id)


def function(computer_array):
    if len(computer_array)==0:
        return []
    if "AMD" in computer_array[0].cpu and "NVIDIA GTX30" in computer_array[0].gpu and computer_array[0].ram >= 16:
        return [computer_array[0]] + function(computer_array[1:])
    else:
        return function(computer_array[1:])


computer_array = []
computer_array.append(Computer("INTEL i7-860", "NVIDIA GTX3080", 16))
computer_array.append(Computer("AMD 5900x", "NVIDIA GTX3080", 32))
computer_array.append(Computer("INTEL i9-10900T", "NVIDIA GTX1070", 8))
computer_array.append(Computer("AMD 5900x", "AMD RX6900", 8))
computer_array.append(Computer("AMD 5700", "AMD RX6900", 16))
computer_array.append(Computer("AMD 5900x", "NVIDIA GTX3090", 64))
computer_array.append(Computer("INTEL i5-8400", "NVIDIA GTX1060", 4))
print(function(computer_array))



########################################################################################################################
#condition_sum_higher_order

from functools import reduce


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
#condition_sum_list_comprehension

from functools import reduce


def function(n):
    array_data = [value for value in range(2, n + 1) if value % 3 == 0 or value % 4 == 0]
    total = 0
    scanned = [total := total + x for x in array_data]
    return scanned[-1]


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

from functools import reduce


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
#find_list_comprehension

from functools import reduce


def function(data_array, element):
    return [idx for (idx, value) in enumerate(data_array) if value == element][0]


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
#is_prime_list_comprehension

def function(number):
    return len([value for value in range(1, number+1) if number % value == 0]) == 2


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
#LinkedList_higher_order

from functools import reduce
from itertools import accumulate


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)

    def __iter__(self):
        self.current = self
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            tmp = self.current
            self.current = self.current.next
            return tmp


def function(node_list):
    filtered_list = filter(lambda x: x[0] % 2 == 0, enumerate(node_list))
    mapped_list = map(lambda x: x[1].data, filtered_list)
    return reduce(lambda x, y: x + y, mapped_list)


node1 = Node(2)
node2 = Node(5)
node3 = Node(7)
node4 = Node(4)
node5 = Node(1)
node6 = Node(3)
node7 = Node(6)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
print(function(node1))



########################################################################################################################
#LinkedList_iterative


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)

    def __iter__(self):
        self.current = self
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            tmp = self.current
            self.current = self.current.next
            return tmp


def function(node_list):
    result = 0
    for idx, node in enumerate(node_list):
        if idx % 2 == 0:
            result += node.data
    return result

node1 = Node(2)
node2 = Node(5)
node3 = Node(7)
node4 = Node(4)
node5 = Node(1)
node6 = Node(3)
node7 = Node(6)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
print(function(node1))



########################################################################################################################
#LinkedList_list_comprehension

from functools import reduce
from itertools import accumulate


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)

    def __iter__(self):
        self.current = self
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            tmp = self.current
            self.current = self.current.next
            return tmp


def function(node_list):
    filtered_list = [node.data for (idx, node) in enumerate(node_list) if idx % 2 == 0]
    total = 0
    scanned = [total := total + x for x in filtered_list]
    return scanned[-1]


node1 = Node(2)
node2 = Node(5)
node3 = Node(7)
node4 = Node(4)
node5 = Node(1)
node6 = Node(3)
node7 = Node(6)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
print(function(node1))



########################################################################################################################
#LinkedList_recursive

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)


def function(node_list, odd=False):
    if node_list is None:
        return 0
    if not odd:
        return node_list.data + function(node_list.next, True)
    else:
        return function(node_list.next, False)


node1 = Node(2)
node2 = Node(5)
node3 = Node(7)
node4 = Node(4)
node5 = Node(1)
node6 = Node(3)
node7 = Node(6)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
print(function(node1))



########################################################################################################################
#max_higher_order

from functools import reduce


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
#max_list_comprehension

from functools import reduce


def function(array_data):
    max_value = array_data[0]
    scanned = [max_value := x for x in array_data if x > max_value]
    return scanned[-1]


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

from itertools import product
from functools import reduce


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
#node_list_comprehension

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
    multiplies = [x.value * y.value for x in node.pre_order_iter() for y in node.pre_order_iter()]
    total = 0
    scanned = [total := total + x for x in multiplies]
    return scanned[-1]


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
#prime_factors_list_comprehension

def helper(number):
    return len([value for value in range(1, number + 1) if number % value == 0]) == 2


def function(number):
    return [x for x in range(2, number + 1) if helper(x) and number % x == 0]


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

from functools import reduce


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
#quad_mul_list_comprehension

from functools import reduce


def function(n):
    array_data = [x**2 for x in range(1, n + 1)]
    total = 1
    scanned = [total := total * x for x in array_data]
    return scanned[-1]


print(function(3))



########################################################################################################################
#quad_mul_recursive

def function(n):
    if n == 1:
        return 1
    return n ** 2 * function(n - 1)


print(function(3))



########################################################################################################################
#Store_higher_order

from itertools import product


class Store:
    id = 0

    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.orders = []
        self.id = Store.id
        Store.id += 1

    def add_order(self, order_id):
        self.orders.append(order_id)

    def __repr__(self):
        return str(self.id)


class Order:
    id = 0

    def __init__(self, product_name, number, price):
        self.product_name = product_name
        self.magnitude = number
        self.price = price
        self.id = Order.id
        Order.id += 1

    def __repr__(self):
        return str(self.id)


def function(store_array, order_array):
    selected_stores = filter(lambda x: x.name == "Edeka", store_array)
    selected_orders = filter(lambda x: x.product_name == "sour cream", order_array)
    selected_product = product(selected_stores, selected_orders)
    selected_stores_with_products = filter(lambda tuple: tuple[1].id in tuple[0].orders, selected_product)
    return list(map(lambda x: x[0], selected_stores_with_products))


store_array = []
store_array.append(Store("Edeka", "Leipzig"))
store_array.append(Store("Rewe", "München"))
store_array.append(Store("Lidl", "Leipzig"))
store_array.append(Store("Edeka", "Berlin"))

order_array = []
order_array.append(Order("sour cream", 100, 0.9))
order_array.append(Order("cheese", 230, 1.2))
order_array.append(Order("apples", 40, 0.5))
order_array.append(Order("potatoes", 2000, 0.2))
order_array.append(Order("pans", 10, 10.9))

store_array[0].add_order(0)
store_array[0].add_order(2)
store_array[0].add_order(4)
store_array[1].add_order(1)
store_array[1].add_order(3)
store_array[2].add_order(2)
store_array[2].add_order(0)
store_array[2].add_order(1)
store_array[3].add_order(0)

print(function(store_array, order_array))



########################################################################################################################
#Store_iterative

from itertools import product


class Store:
    id = 0

    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.orders = []
        self.id = Store.id
        Store.id += 1

    def add_order(self, order_id):
        self.orders.append(order_id)

    def __repr__(self):
        return str(self.id)


class Order:
    id = 0

    def __init__(self, product_name, number, price):
        self.product_name = product_name
        self.magnitude = number
        self.price = price
        self.id = Order.id
        Order.id += 1

    def __repr__(self):
        return str(self.id)


def function(store_array, order_array):
    stores = []
    for store in store_array:
        if store.name == "Edeka":
            stores.append(store)

    orders = []
    for order in order_array:
        if order.product_name == "sour cream":
            orders.append(order)

    result = []
    for store in stores:
        for order in orders:
            if order.id in store.orders:
                result.append(store)

    return result


store_array = []
store_array.append(Store("Edeka", "Leipzig"))
store_array.append(Store("Rewe", "München"))
store_array.append(Store("Lidl", "Leipzig"))
store_array.append(Store("Edeka", "Berlin"))

order_array = []
order_array.append(Order("sour cream", 100, 0.9))
order_array.append(Order("cheese", 230, 1.2))
order_array.append(Order("apples", 40, 0.5))
order_array.append(Order("potatoes", 2000, 0.2))
order_array.append(Order("pans", 10, 10.9))

store_array[0].add_order(0)
store_array[0].add_order(2)
store_array[0].add_order(4)
store_array[1].add_order(1)
store_array[1].add_order(3)
store_array[2].add_order(2)
store_array[2].add_order(0)
store_array[2].add_order(1)
store_array[3].add_order(0)

print(function(store_array, order_array))



########################################################################################################################
#Store_list_comprehension

from itertools import product


class Store:
    id = 0

    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.orders = []
        self.id = Store.id
        Store.id += 1

    def add_order(self, order_id):
        self.orders.append(order_id)

    def __repr__(self):
        return str(self.id)


class Order:
    id = 0

    def __init__(self, product_name, number, price):
        self.product_name = product_name
        self.magnitude = number
        self.price = price
        self.id = Order.id
        Order.id += 1

    def __repr__(self):
        return str(self.id)


def function(store_array, order_array):
    selected_stores = [store for store in store_array if store.name == "Edeka"]
    selected_orders = [order for order in order_array if order.product_name == "sour cream"]
    return [store for store in selected_stores for order in selected_orders if order.id in store.orders]


store_array = []
store_array.append(Store("Edeka", "Leipzig"))
store_array.append(Store("Rewe", "München"))
store_array.append(Store("Lidl", "Leipzig"))
store_array.append(Store("Edeka", "Berlin"))

order_array = []
order_array.append(Order("sour cream", 100, 0.9))
order_array.append(Order("cheese", 230, 1.2))
order_array.append(Order("apples", 40, 0.5))
order_array.append(Order("potatoes", 2000, 0.2))
order_array.append(Order("pans", 10, 10.9))

store_array[0].add_order(0)
store_array[0].add_order(2)
store_array[0].add_order(4)
store_array[1].add_order(1)
store_array[1].add_order(3)
store_array[2].add_order(2)
store_array[2].add_order(0)
store_array[2].add_order(1)
store_array[3].add_order(0)

print(function(store_array, order_array))



########################################################################################################################
#Store_recursive

from itertools import product


class Store:
    id = 0

    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.orders = []
        self.id = Store.id
        Store.id += 1

    def add_order(self, order_id):
        self.orders.append(order_id)

    def __repr__(self):
        return str(self.id)


class Order:
    id = 0

    def __init__(self, product_name, number, price):
        self.product_name = product_name
        self.magnitude = number
        self.price = price
        self.id = Order.id
        Order.id += 1

    def __repr__(self):
        return str(self.id)

def helper1(order_array):
    if len(order_array) == 0:
        return []
    if order_array[0].product_name == "sour cream":
        return [order_array[0]] + helper1(order_array[1:])
    else:
        return helper1(order_array[1:])


def helper2(store, order_array):
    if len(order_array) == 0:
        return False
    if order_array[0].id in store.orders:
        return True
    else:
        return helper2(store, order_array[1:])


def function(store_array, order_array):
    if len(store_array)==0:
        return []
    if store_array[0].name == "Edeka":
        orders = helper1(order_array)
        if helper2(store_array[0], orders):
            return [store_array[0]] + function(store_array[1:], order_array)

    return function(store_array[1:], order_array)


store_array = []
store_array.append(Store("Edeka", "Leipzig"))
store_array.append(Store("Rewe", "München"))
store_array.append(Store("Lidl", "Leipzig"))
store_array.append(Store("Edeka", "Berlin"))

order_array = []
order_array.append(Order("sour cream", 100, 0.9))
order_array.append(Order("cheese", 230, 1.2))
order_array.append(Order("apples", 40, 0.5))
order_array.append(Order("potatoes", 2000, 0.2))
order_array.append(Order("pans", 10, 10.9))

store_array[0].add_order(0)
store_array[0].add_order(2)
store_array[0].add_order(4)
store_array[1].add_order(1)
store_array[1].add_order(3)
store_array[2].add_order(2)
store_array[2].add_order(0)
store_array[2].add_order(1)
store_array[3].add_order(0)

print(function(store_array, order_array))



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
#students_list_comprehension

class Student:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def __repr__(self):
        return str(self.name)


def function(student_array):
    return [student for student in student_array if student.age >= 18]


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



