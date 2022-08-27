class Car:
    def __init__(self, model, price):
        self.model = model
        self.price = price


class CarFactory:
    model = 'Opel'
    common_price = 10000

    def build(self, count=1):
        cars = []

        for i in range(count):
            cars.append(Car(self.model, self.common_price))

        return cars


class CapacityEx(Exception):
    def __init__(self, current, need):
        self.current = current
        self.need = need

    def __str__(self):
        return f"Недостаточно пространства для размещения {self.current} машин, необходимо еще {self.need}"


class CarStock:
    def __init__(self, count=0):
        self.max_count = count
        self.cars = []

    def store(self, cars):
        # TODO проверка вместимости склада
        if len(cars) >= self.max_count:
            raise CapacityEx(len(cars), len(self.cars) + len(cars) - self.max_count)
        self.cars.extend(cars)


class NotEnMoneyEx(Exception):
    def __init__(self, current, need):
        self.current = current
        self.need = need

    def __str__(self):
        return f"Недостаточно средств {self.current}, необходимо еще {self.need}"


class Customer:
    def __init__(self, money):
        self.money = money

    def buy(self, car):
        # TODO проверка текущего баланса
        if car.price > self.money:
            raise NotEnMoneyEx(self.money, car.price)
        self.money -= car.price


factory = CarFactory()
stock = CarStock(1)
customer_1 = Customer(1234)

car_list = factory.build(4)

try:
    stock.store(car_list)
    customer_1.buy(stock.cars[1])
except (NotEnMoneyEx, CapacityEx) as err:
    print(err)
print(customer_1.money)
