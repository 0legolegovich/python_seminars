# Семинар 2 Задача 4:
# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

# Заполнение массива случайными числами из промежутка [-N, N]
import random
number = int(input("Введите число N: "))
array=[]
for i in range (number):
    array.append(random.randrange(-number, number))
print(array)

# Выбор индексов элементов для перемножения 
print("Введите индексы элементов для перемножения. После окончания ввода нажмите 'q'")
indices = []
index = 0
product = 1
while index != 'q':
    index = input("")
    if index != 'q':
        indices.append(int(index))

# Перемножение элементов под выбранными индексами
for i in range(len(indices)):
    product = product * array[indices[i]]
print("Произведение элементов составило " + str(product))
