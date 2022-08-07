# 6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.


# решение с вводом всего предложения внутри функции
# def int_func():
#     latin_char = list(range(97, 123))  # ascii lowercase 97 - 123
#     for word in input('Введите предложение из маленьких латинских букв разделяя слова пробелами:\n ').split(' '):
#         char = 0
#         for elem in list(map(ord, word)):
#             if elem in latin_char:
#                 char += 1
#         print(word.capitalize()) if (len(word) == char) else print('ОШИБКА: только маленькие латинские буквы')
#
#
# print(int_func())


def int_func(word):
    latin_char = ''.join(map(chr, range(97, 123)))
    return word.capitalize() if not set(word).difference(latin_char) else False


sentence = input('Введите предложение из маленьких латинских букв разделяя слова пробелами:\n ').split(' ')
for elem in sentence:
    result = int_func(elem)
    if result:
        print(result, ' ')
