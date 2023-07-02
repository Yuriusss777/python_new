# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.
# Пример:
# [1, 2, 3, 1, 2, 4, 5] -> [1, 2]


my_list = [1, 2, 3, 1, 2, 4, 5]
my_list_new = sorted(my_list)
my_list_1 = []

for i in range(len(my_list_new) - 1):
    if my_list_new[i] == my_list_new[i + 1]:
        my_list_1.append(my_list_new[i])
    continue

print(my_list_1)
