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
