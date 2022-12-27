# Семинар 4 Задача 4
# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

import random
power = int(input('Введите натуральную степень k: '))

# В результате выполнения программы получаем строчное представление многочлена, степень представлена в виде х5, х4 и т.д. для удобства.
# Для выполнения математических операций можно пользоваться списком array с коэффициентами многочлена

array = []
expression = ''
for i in range (power + 1):
    array.append(random.randrange(-100, 100))
    if array[i] == 0:
        continue
    elif array[i] > 0:
        expression = ' + ' + str(array[i]) + '*x' + str(i) + expression
    else:
        expression = ' - ' + str(-array[i]) + '*x' + str(i) + expression
if expression[1] =='+':
    expression = expression[2:-3] + ' = 0'
else:
    expression = expression[:-3] + ' = 0'
print("Коэффициенты многочлена, от меньшего к большему:")
print(array)
print('Многочлен степени k:')
print(expression)

with open('file_DZ4-4.txt', 'w') as data:
    data.write(expression)
data.close()

