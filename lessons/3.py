# создание функции
def my_fucking_def():
    """строки документирования функции"""
    pass  # заглушка, еще можно так ...


# примеры на уроке
def my_f(a, n_1=10, n_2=9):
    sub = n_1 - n_2
    if a == 1:
        return sub, False, 77
    else:
        return [sub, False, 77]


result = my_f(0, int(input("n_1: ")), int(input("n_2: ")))
print(result * 4)


# kwargs возвращает словарь
def my_f2(**kwargs):
    return kwargs


# print(my_f2(n_1=1, n_2=2))

#  лямбда
my_f3 = lambda n_1, n_2: n_1 - n_2

print((lambda *args: args)(45, 6, 45, 6))

# встроенные функции
abs(-90)  # по модулю
round(1.2341)  # округление
divmod(9, 5)  # деление
pow(2, 5)  # степень
max(1, 2, 3, 4)  # можно передать key - и определить тип данных для сравнения
min(1, 2, 3, 4)  #
sum([1, 2, 3, 4])  # не умеет 1,2,3,4; не умеет 12345, надо делать [1,2,3,4]


# области видимости
def full_s_calc():
    global s_circle
    r_val = float(input(""))
    h_val = float(input(""))
    s_side = 2 * 3.14 * r_val * h_val
    s_circle = 3.14 * r_val ** 2
    s_full = s_side + 2 * s_circle


# map
a = [3, 4, 5, 2, 7, 8]
b = [7, 9, 2, 4, 5, 1]
c = [5, 7, 3, 4, 5, 8]
dict_a = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]
print(list(map(lambda x, y, z: x + y + z, a, b, c)))
print(list(filter(lambda x: x % 2 == 0, a)))
