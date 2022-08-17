# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# © geekbrains.ru 24
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные. При
# этом английские числительные должны заменяться на русские. Новый блок строк должен
# записываться в новый текстовый файл.

my_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
with open("5_4_new.txt", "w", encoding="utf-8") as new_file:
    with open("5_4.txt", "r", encoding="utf-8") as file:
        new_file.writelines([line.replace(line.split()[0], my_dict.get(line.split()[0])) for line in file])


# не построчно, но перебор по словарю
# my_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
# with open("5_4.txt", "r", encoding="utf-8") as file:
#     s = file.read()
#     for key, val in my_dict.items():
#         s = s.replace(key, val)
# open("5_4_new.txt", "w", encoding="utf-8").write(s)
