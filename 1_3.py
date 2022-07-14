# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.


num_str = input('Введите целое число: ')
i = 1
sum_of_num = 0
while i <= 3:
    if num_str[0] == '-':
        num = '-' + num_str[1:] * i
    else:
        num = num_str * i
    sum_of_num = sum_of_num + int(num)
    i += 1

print(sum_of_num)
