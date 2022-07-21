# 2. Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().

my_list = input('Введите элементы списка через запятую: ').split(',')
print(f'Заданный список: {my_list}')

# решение 1
# i = 0
# for elem in my_list[1:]:
#     if my_list.index(elem) % 2 == 1:
#         my_list.insert(i, elem)
#         i += 2
#         my_list.pop(i)
#

# решение 2
# i = 0
# for elem in my_list[1:2:]:
#     my_list.insert(i, elem)
#     i += 2
#     my_list.pop(i)

# решение 3
for i in range(1, len(my_list), 2):
    my_list[i], my_list[i-1] = my_list[i-1], my_list[i]


print(f'Отсортированный список: {my_list}')
