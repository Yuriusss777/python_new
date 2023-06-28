# Напишите программу, которая принимает две строки
# вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму
# и *произведение дробей. Для проверки своего
# кода используйте модуль fractions.
# Пример:
# # Ввод:
# 1/2
# 1/3
# Вывод: 5/6 1/6

number_1 = input('Введите дробное число 1: ')
number_2 = input('Введите дробное число 2: ')

number_3 = number_1.split('/')
number_4 = number_2.split('/')
# sum_1 = number_3[0] * number_4[1] + number_3[1] * number_4[0]
a = int(number_3[0])
b = int(number_3[1])
c = int(number_4[0])
d = int(number_4[1])

sum_add = f'{a * d + b * c} / {(b * d)}'
composition = f'{a * c} / {b * d}'

print(f'Сумма дробей = {sum_add}, Произведение дробей = {composition}')
