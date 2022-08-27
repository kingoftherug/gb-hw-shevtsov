# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

# високосные года 1764, 1768, 1772
from math import floor


class Data:

    def __init__(self, d: str):
        self.date_str = d
        date_list = d.split('-')
        self.day, self.month, self.year = self.str_to_int(date_list)

        if not self.date_validator(self.day, self.month, self.year):
            raise ValueError(f"{d} неверный формат даты")

    def __str__(self):
        return f'{self.date_str} - все ок'

    @staticmethod
    def date_validator(d: int, m: int, y: int):
        leap_year = bool(not (y % 400 and y % 4) and y % 100)
        last_day = 28 + (m + floor(m / 8)) % 2 + 2 % m + 2 * floor(1 / m)
        last_day += leap_year if m == 2 else 0
        return all([1 <= d <= last_day, 1 <= m <= 12, y >= 1970])

    @classmethod
    def str_to_int(cls, str_list):
        return [int(i) for i in str_list]


dates = ['01.02.2022', '01-20-2020', 'xx-xx-2020', '29-02-1991', '29-02-2024', '10-10-10-10']

for date in dates:
    try:
        print(Data(date))
    except ValueError as e:
        print(e)
