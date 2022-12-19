# Семинар 2 Задача 2:
# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
number = int(input("Введите число N: "))
result = 1
result_list = []
for i in range(1, number + 1):
    result = result * i 
    result_list.append(result)
print (result_list)
