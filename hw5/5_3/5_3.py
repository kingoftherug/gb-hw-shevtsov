# Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и
# величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее
# 20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода
# сотрудников.

def employee_list_with_min_salary(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        return [i.split()[0] for i in file if float(i.split()[1]) < 20000]


def salary_avg(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        salary_list = [float(i.split()[1]) for i in file]
        return sum(salary_list) / len(salary_list)


print(f'Сотрудники с ЗП меньше 20тысяч: {employee_list_with_min_salary("5_3.txt")}')
print(f'Средняя ЗП: {salary_avg("5_3.txt")}')
