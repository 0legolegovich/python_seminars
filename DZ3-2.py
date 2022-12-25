# Семинар 3 Задача 2:
# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Заполнение массива случайными числами из промежутка [-N, N]
import random
number = int(input("Введите количество элементов списка: "))
array=[]
for i in range (number):
    array.append(random.randrange(-number, number))
print(array)

#Произведение пар чисел списка
product = 1
product_array = []
for i in range(len(array) // 2 + 1):
    product = array[i] * array [len(array) - 1 - i]
    product_array.append(product)
print(product_array)


