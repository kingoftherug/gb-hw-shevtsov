# 4. Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов.
# В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.


class Warehouse:
    def __init__(self, count=0):
        self.max_count = count
        self.items = []


class OfficeEquipment:
    def __init__(self, article, model, brand, price: float):
        self.article = article
        self.name = model
        self.brand = brand
        self.price = price


class Printer(OfficeEquipment):
    def __init__(self, article, model, brand, price: float, is_colored=False, print_type='Струйный'):
        super().__init__(article, model, brand, price)
        self.is_colored = is_colored
        self.print_type = print_type


class Scanner(OfficeEquipment):
    def __init__(self, article, model, brand, price: float, is_colored=False, scan_type='Барабанный'):
        super().__init__(article, model, brand, price)
        self.is_colored = is_colored
        self.scan_type = scan_type


class Xerox(OfficeEquipment):
    def __init__(self, article, model, brand, price: float, xerox_type='Портативные'):
        super().__init__(article, model, brand, price)
        self.xerox_type = xerox_type



