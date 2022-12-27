# Семинар 4 Задача 2
# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

number = int(input('Задайте натуральное число N: '))

# Список простых чисел от 2 до N (заданного пользователем числа)
# Число является простым, если оно не делится на предыдущие числа списка простых чисел
# Делитель составного числа в пределах k/2
prime_numbers_list = [2]
for k in range(3, number, 2):
    i = 0
    while k > prime_numbers_list[i]:
        if k % prime_numbers_list[i] == 0:
            break
        if prime_numbers_list[i] * 2 > k:
           prime_numbers_list.append(k)
           break
        i +=1
# print(prime_numbers_list)

# Составление списка простых множителей
factors_list = []
for i in range(len(prime_numbers_list)):
    while number % prime_numbers_list[i] == 0:
        factors_list.append(prime_numbers_list[i])
        number = number / prime_numbers_list[i]
print(factors_list)
