# Семинар 2 Задача 1
# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
number = input("Введите вещественное число: ")
sum = 0
for digit in number:
    if digit=="." or digit==",":
        continue
    else:
        sum = sum + int(digit)
print (sum)
