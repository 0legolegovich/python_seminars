# Семинар 2 Задача 3:
# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
number = int(input("Введите число N: "))
result_list = []
sum = 0
for i in range(1, number + 1):
    result = pow((1 + 1 / i), i) 
    result_list.append(result)
    sum = sum + result
print (result_list)
print (sum)