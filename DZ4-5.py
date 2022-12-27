# Семинар 4 Задача 5
# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

import random
power = int(input('Введите натуральную степень k: '))

# В результате выполнения программы получаем строчное представление многочлена, степень представлена в виде х5, х4 и т.д. для удобства.
# Для выполнения математических операций проще всего пользоваться списком array с коэффициентами многочлена. В связи с этим в искомых файлах считаю наиболее разумным хранить списки с коэффициентами многочленов.

# Создание списка с коэфициентами первого многочлена
array1 = []
for i in range (power + 1):
    array1.append(random.randrange(-100, 100))
print("Коэффициенты многочлена 1, от меньшего к большему:")
print(array1)

with open('file_DZ4-5_exp1.txt', 'w') as data:
    for element in array1:
        data.write(str(element) + ',')
data.close()

# Создание списка с коэфициентами второго многочлена
array2 = []
for i in range (power + 1):
    array2.append(random.randrange(-100, 100))
print("Коэффициенты многочлена 2, от меньшего к большему:")
print(array2)

with open('file_DZ4-5_exp2.txt', 'w') as data:
    for element in array2:
        data.write(str(element) + ',')
data.close()

print('Коэфициенты этих многочленов записаны в файл с использованием запятой как разделителя')

# Функция чтения коэффициентов из файла и их записи в список
def read_from_file(file_name):
    temp = ''
    temp2 = ''
    read_data=[]
    data = open(file_name, 'r')
    for char in data:
        temp += char
    for char in temp:
        if char != ",":
            temp2 += char
        else:
            read_data.append(int(temp2))
            temp2 = ''
    data.close()
    return read_data

print()

res1 = read_from_file('file_DZ4-5_exp1.txt')
res2 = read_from_file('file_DZ4-5_exp2.txt')
print('Списки коэфициентов многочленов, прочитанные из файлов:')
print(res1)
print(res2)
print()

res = []
for i in range(len(res1)):
    res.append(res1[i] + res2[i])
print('Список коэфициентов, полученных в результате суммы:')
print(res)
print()

# Вывод результирующего многочлена
expression = ''
for i in range (len(res)):
    if res[i] == 0:
        continue
    elif res[i] > 0:
        expression = ' + ' + str(res[i]) + '*x' + str(i) + expression
    else:
        expression = ' - ' + str(-res[i]) + '*x' + str(i) + expression
if expression[1] =='+':
    expression = expression[2:-3] + ' = 0'
else:
    expression = expression[:-3] + ' = 0'
print('Сумма многочленов:')
print(expression)

# Запись результирующего многочлена в файл
with open('file_DZ4-5.txt', 'w') as data:
    data.write(expression)
data.close()