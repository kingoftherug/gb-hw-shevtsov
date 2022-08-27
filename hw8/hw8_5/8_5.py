# 5. Продолжить работу над первым заданием.
# Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру (например, словарь).


class Warehouse:
    def __init__(self, count=0):
        self.max_count = count
        self.items = []

    def eq_input(self, items):
        # TODO добавить проверку что не превышена емкость склада
        self.items.append(items)

    def eq_output(self, article):
        # TODO добавить проверку что сток не меньше нуля
        # TODO добавить удаление из списка по артиклю
        pass


class OfficeEquipment:
    def __init__(self, article, model, brand, price: float):
        self.article = article
        self.model = model
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


warehouse = Warehouse(100)
printer_1 = Printer('001', '111', 'EPSON', 1000)
printer_2 = Printer('002', '111', 'EPSON', 1000)
printer_3 = Printer('003', '222', 'EPSON', 2000, True)
printer_4 = Printer('004', 'xxx', 'Samsung', 3000, True)
scanner_1 = Scanner('005', 'qwerty', 'CAD CAM', 1_000_000, True, '3D')

warehouse.eq_input([printer_1, printer_2, printer_3, printer_4, scanner_1])
print(warehouse)
