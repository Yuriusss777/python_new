# Дополнительное:
# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
# числа используйте код:


from random import randint

num = randint(0, 1000)

# if num > 750:
#     if num > 875:
#         if num > 937:
#             if num > 968:
#                 if num > 984:
#                     if num > 992:
#                         if num > 996:
#                             if num > 998:
#                                 print( if a == num)


for i in range(1, 11):
    a = int(input(f'Введите попытку {i}: '))
    if a == num:
        print("Вы угадали число")
        break
    elif num < a:
        print(f"num меньше {a}")
        continue
    elif num > a:
        print(f"num больше {a}")


