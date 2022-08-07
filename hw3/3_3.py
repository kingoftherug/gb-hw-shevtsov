# 3. Реализовать функцию my_func(),
# которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.

# мой вариант
def my_func(num1, num2, num3):
    """функция определения наибольшей суммы 2х чисел из 3х"""
    f_list = [num1, num2, num3]
    f_list.sort(reverse=True)
    return sum(f_list[:2])


print(my_func(10, 3, 15))

# варианты из разбора дз 1

# def my_func(num_1, num_2, num_3):
#     try:
#         my_list = list(map(float, [num_1, num_2, num_3]))
#         my_list.remove(min(my_list))
#         return sum(my_list)
#     except (TypeError, ValueError):
#         return "Можно вводить только числа"

# вариант из разбора дз 2

# def my_func(arg1, arg2, arg3):
#     return sum(sorted([arg1, arg2, arg3])[1:])

# вариант из разбора дз 3 lambda

# my_func = lambda arg_1, arg_2, arg_3: (arg_1 + arg_2 + arg_3) - min(arg_1, arg_2, arg_3)
# print(my_func(10, 3, 15))
