class Car:
    id = 0

    def __init__(self, color, hp, electrical, brand):
        self.color = color
        self.hp = hp
        self.electrical = electrical
        self.brand = brand
        self.id = Car.id
        Car.id += 1

    def __repr__(self):
        return str(self.id)


def function(car_array):
    return list(filter(lambda x: x.brand == "Tesla" or x.brand == "Nissan" and x.hp >= 100, car_array))


car_array = []
car_array.append(Car("red", 700, True, "Tesla"))
car_array.append(Car("black", 140, False, "Nissan"))
car_array.append(Car("white", 90, False, "Nissan"))
car_array.append(Car("yellow", 80, True, "Mini"))
car_array.append(Car("blue", 200, True, "Tesla"))
car_array.append(Car("green", 120, False, "Mercedes"))
car_array.append(Car("red", 700, True, "Tesla"))
print(function(car_array))
