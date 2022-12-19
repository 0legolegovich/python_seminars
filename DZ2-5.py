# Семинар 2 Задача 5:
# Реализуйте алгоритм перемешивания списка.

# Заполнение массива случайными числами из промежутка [0, N]
import random
number = int(input("Введите число N: "))
array=[]
for i in range (number):
    array.append(random.randrange(-number, number))
print(array)

#Перемешивание списка 1
random.shuffle(array)
print(array)

#Перемешивание списка 2
array2 = random.sample(array, len(array))
print (array)
