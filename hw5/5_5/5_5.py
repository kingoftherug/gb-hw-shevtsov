#  Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых
# пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

from hw4.lib4 import my_list

with open("5_5.txt", "w", encoding="utf-8") as file:
    file.write(' '.join(map(str, my_list)))
print(f'сумма чисел списка: {sum(my_list)}')

# # из разбора дз
# from random import randint
#
# with open("5_5.txt", "w+", encoding="utf-8") as file:
#     file.write(" ".join([str(randint(1, 100)) for _ in range(100)]))
#     file.seek(0)
#     print(sum(map(int, file.readline().split())))
