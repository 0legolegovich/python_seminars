# Семинар 4 Задача 1
# Вычислить число pi c заданной точностью d

accuracy = int(input('Задайте точность вычисления числа pi (количество знаков после запятой): '))
import math
print(round(math.pi, accuracy))
