# Семинар 3 Задача 3:
# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Заполнение массива случайными вещественными числами из промежутка
import random
number = int(input("Введите количество элементов списка: "))
array=[]
for i in range (number):
    array.append(random.randrange(0, 10000)/100)
print(array)

#Отбрасываем целую часть, выводим результат
after_comma_array = []
for i in range (len(array)):
    after_comma_array.append(array[i] - int(array[i]))
    after_comma_array[i] = round(after_comma_array[i], 2)
print(after_comma_array)

#Находим минимум, максимум и разницу между ними

min = after_comma_array[0]
max = after_comma_array[0]
for i in range (len(after_comma_array)):
    if after_comma_array[i] > max:
        max = after_comma_array[i]
    if after_comma_array[i] < min:
        min = after_comma_array[i]
result = max - min
print("Результат равен " + str(round(result, 2)))
