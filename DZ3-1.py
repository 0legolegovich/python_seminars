# Семинар 3 Задача 1:
# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Заполнение массива случайными числами из промежутка [-N, N]
import random
number = int(input("Введите количество элементов списка: "))
array=[]
for i in range (number):
    array.append(random.randrange(-number, number))
print(array)

#Вывод элементов из списка, стоящих на нечетных позициях, и их суммы 
sum = 0
print("[", end="")
for i in range(1, len(array), 2):
    sum = sum + array[i]
    if i==len(array) - 1 or i==len(array) - 2:
        print(str(array[i]) + "]")
        print("Сумма = " + str(sum))
    else:
        print(array[i], end=", ")
        
