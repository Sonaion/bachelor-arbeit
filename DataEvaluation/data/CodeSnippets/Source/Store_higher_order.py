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
