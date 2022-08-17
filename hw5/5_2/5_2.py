# Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить
# подсчёт строк и слов в каждой строке.

with open('5_2.txt', 'r', encoding='utf-8') as file:
    for count, line in enumerate(file, 1):
        c = line.split()
        print(f'в строке {count} слов: {len(c)}')
