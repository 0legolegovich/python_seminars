# Семинар 3 Задача 4:
# Напишите программу, которая будет преобразовывать десятичное число в двоичное.


number_decimal = int(input("Введите десятичное число: "))
number_binary = ''
while number_decimal > 0:
    # Остаток от деления на два преобразуется в строку и добавляется к концу строчной переменной
    number_binary = str(number_decimal % 2) + number_binary
    number_decimal = number_decimal // 2
print(number_binary)