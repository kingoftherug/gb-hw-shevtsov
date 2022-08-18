# 3. Реализовать базовый класс Worker (работник).
# ● определить атрибуты: name, surname, position (должность), income (доход);
# ● последний атрибут должен быть защищённым и ссылаться на словарь, содержащий
# элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
# ● создать класс Position (должность) на базе класса Worker;
# ● в классе Position реализовать методы получения полного имени сотрудника
# (get_full_name) и дохода с учётом премии (get_total_income);
# ● проверить работу примера на реальных данных: создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров.

# базовый класс
class Worker:
    _income = {"wage": None, "bonus": None}

    def __init__(self, n, s, p, i):
        self.name = n
        self.surname = s
        self.position = p
        self._income = i


class Position(Worker):
    def get_full_name(self):
        print(f'{self.name} {self.surname}')

    def get_total_income(self):
        print(f'{self._income["wage"] + self._income["bonus"]}')


employee_1 = Position("Василий", "Иванов", "Слесарь", {"wage": 100000, "bonus": 50000})
employee_1.get_full_name()
employee_1.get_total_income()
employee_2 = Position("Иван", "Васильев", "Руководитель", {"wage": 9000, "bonus": 150000})
employee_2.get_full_name()
employee_2.get_total_income()
