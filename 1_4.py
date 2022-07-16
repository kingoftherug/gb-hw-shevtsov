# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.


num = int(input('Введите целое положительное число: '))
big_num = 0
i = 0
while num > 0:
    i += 1
    num_candidate = num % 10
    # раскомментируйте строку ниже для проверки
    # print('step id: {}, num_candidate: {}, big_num: {}'.format(i, num_candidate, big_num))
    num = num // 10
    if num_candidate == 9:
        big_num = num_candidate
        break
    elif num_candidate > big_num:
        big_num = num_candidate

print(big_num)
