# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N.
# Выведите, ближайший к X элемент. Если есть несколько элементов, которые равноудалены от X, выведите наименьший по величине.
# Ввод: 10
# Ввод: 7
# 1 2 1 8 9 6 5 4 3 4
# Вывод: 6
import random
n = int(input('Введите размер массива: '))
x = int(input('Введите число, которое нужно проверить: '))
list_1 = list()
for i in range(0,n):
    n = round(random.randint(0,10))
    list_1.append(n)
print(list_1)

num = list_1[0]
a = abs(x - list_1[0])
for i in range(1, len(list_1)):
    if a > abs(list_1[i] - x):
        a = abs(list_1[i] - x)
        num = list_1[i]
print(num)

