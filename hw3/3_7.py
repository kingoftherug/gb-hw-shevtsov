# 7. Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Нужно сделать вывод исходной строки,
# но каждое слово должно начинаться с заглавной буквы. Используйте написанную ранее функцию int_func().

def int_func(word):
    latin_char = ''.join(map(chr, range(97, 123)))
    return word.capitalize() if not set(word).difference(latin_char) else ''


sentence = input('Введите предложение из маленьких латинских букв разделяя слова пробелами:\n ').split(' ')
print(' '.join(map(int_func, sentence)))
