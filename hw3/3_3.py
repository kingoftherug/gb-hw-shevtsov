# 3. Реализовать функцию my_func(),
# которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.


def my_func(num1, num2, num3):
    """функция определения наибольшей суммы 2х чисел из 3х"""
    f_list = [num1, num2, num3]
    f_list.sort(reverse=True)
    return f_list[0] + f_list[1]


print(my_func(10, 3, 15))
