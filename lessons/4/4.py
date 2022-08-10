# # импортирование служебных и собственных модулей
# # import math
# # from math import sin, pi
# # from math import * # вредно, т.к. выгружает всё
# import lib4 as li
#
# li.hi()
# print(li.simple())
# # запуск скрипта с параметрами
from sys import argv

name, n_1, n_2, n_3 = argv
print(argv)
# print((int(n_1) + int(n_2)) * int(n_3))

# # # генераторы списков, словарей и множеств
# # # список
# # my_list = list(range(1, 11))
# # # new_list = [n + 10 for n in my_list if n % 2 == 1]
# # # new_list = [n + 10 if n % 2 == 0 else n ** 3 for n in my_list]
# # new_list = {n ** 3 for n in range(1, 11)}
# # print(new_list)
# # словарь
# # new_list = {k: n ** 3 for k, n in zip("ASDFGHJK", range(1, 11))}
# # print(new_list)
# from itertools import islice
#
# # new_list = (n ** 3 for n in range(1, 1_000_000_000))
# new_list = (n ** 3 for n in range(1, 11))
# print(new_list)
#
# # for i in new_list:
# #     print(i)
#
# print(next(new_list))
# print(next(new_list))
# print(next(new_list))
# print(*islice(new_list, 8))
# new_list = (n ** 3 for n in range(1, 11))
# print(*new_list)
#
# # распаковка
# n = [1, 2, 3, 4]
# print(*n)
# print(*n, sep="\n")
# # comprehension
# # [] - list comprehension
# # {} - set dictionary comprehension
# # () - generator (не получаем готовую структуру, а получаем формулу)

# # модуль random для генерации псевдослучайных чисел
# from random import randint, randrange, random, uniform, choice
#
# print(randint(1, 200))
# print(randrange(2, 22, 2))
# print(random() * 1000)
# print(uniform(2, 5))
# print(choice([1, 2, 3, 4, 5, 6, 75, 574, 34, 2]))

# конструкция yield
def my_f():
    for i in range(1, 11):
        yield i
        print("Hi")


print(my_f())
for i in my_f():
    print(i ** 2)

# модуль fuctools


# модуль itertools


# модуль math
