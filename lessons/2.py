# типы данных
# строки
my_str = 'Python is the best language of the world'

# отрицательная индексация
my_str[-4]
len(my_str)

# слайсы
my_str[0:6]
my_str[600:]

# шаг
my_str[::2]
my_str[1::2]

# реверс
my_str[::-1]

# отрезаем
my_str[:-6]
my_str[-6:]
my_str[35:]

# методы
dir(my_str)

# # разбиение
"1 2 3".split(" ")

# # объединение
" - ".join(["N", "S"])

# # регистр
"сЕрГеЙ".title()
"сЕрГеЙ".capitalize()

# # вхождение
"gipopotampo".count("po")

# # замена
"gipopotampo".replace("po", "")

# # поиск вхождения
"gipopotampo".index("po", 5)
"gipopotampo".find("po", 5)

# список
list("gipopotampo")
my_list = [12, 3.4, "str", False, [1, 2]]

# # разворот
my_list[::-1]

# # добавление
my_list.append(12)

# # распаковка
my_list.extend([11, 22])

# # вставка
my_list.insert(3, True)

# # вхождение
my_list.count(1)
my_list.index(4)

# # изменение значения
my_list[1] = 21

# # удаление
my_list.remove(21)

# # удаление по индексу
my_list.pop(-1)

# # сортировка
my_list = [1, -3, 99, -23, 11]
my_list.sort()
my_list.sort(reverse=True)

# кортеж неизменяемый, но может расширен .append(3)
tuple("gipopotampo").__sizeof__()
list("gipopotampo").__sizeof__()

# множество
set("gipopotampo")
my_set = {12, 2.3, "str", False, (1, 2)}
my_set.add(21)
my_set.remove(21)
my_set.discard(2.3)
my_set.pop()

# словари
my_dict = dict(n=3, m=8)
my_dict = {12: 11, 3.4: 22, False: 33, "str": 44, (1, 2): 44, 66: [1, 2]}

# # поиск по ключу
my_dict[0]
my_dict.get(10, 'Nothing')

# # получить ключи и значения
my_dict.keys()
my_dict.values()
my_dict.items()

# for in
my_list = [12, 3.4, 'str', True, False, [1, 2], 12, 11, 22]
for i in range(len(my_list)):
    # if isinstance(i, list) and 1 in i:
    if isinstance(my_list[i], int):
        my_list[i] **= 2
    print(i)

for i, v in enumerate(my_list, 1):
    print(f"{i}) {v}")

print(my_list)
