# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def my_f(num1, num2):
    """Функция деления двух чисел"""
    try:
        return num1 / num2
    except ZeroDivisionError:
        print('ОШИБКА: Деление на 0')


input_num1 = float(input("Введите первое число: "))
input_num2 = float(input("Введите второе число: "))
print(my_f(input_num1, input_num2))