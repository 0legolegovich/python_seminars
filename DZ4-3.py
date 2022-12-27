# Семинар 4 Задача 3
# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# Заполнение массива случайными числами из промежутка [0, N]
import random
number = int(input("Введите количество элементов списка: "))
array = []
set_from_array = set()
for i in range (number):
    array.append(random.randrange(0, number))
    set_from_array.add(array[i])
print("Введенная последовательность чисел:")
print(array)
print("Список неповторяющихся элементов исходной последовательности:")
print(set_from_array)