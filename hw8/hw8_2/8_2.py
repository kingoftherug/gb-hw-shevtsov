# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.


class CustomZeroD(Exception):
    def __init__(self, che, na_che):
        self.che = che
        self.na_che = na_che

    def __str__(self):
        return f'нельзя {self.che} поделить на {self.na_che}'


class Test:
    def __init__(self, num):
        self.num = num

    def __truediv__(self, other):
        if other.num == 0:
            raise CustomZeroD(self.num, other.num)
        return Test(self.num / other.num)


a = Test(10)
b = Test(0)
try:
    c = a/b
except CustomZeroD as err:
    print(err)
