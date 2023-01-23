# Семинар 3 Задача 5
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

import functools

def fib(n): return list(functools.reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-2), [0, 1]))
#print(fib(10))

def neg_fib(n): return list(map(lambda x: -x, fib(n)))[::-1]
#print(neg_fib(10))

full_fib = neg_fib(10) + fib(10)
print(full_fib)

# number = int(input('Задайте число положительных элементов последовательности: '))

# # Положительный ряд Фибоначчи
# fibonacci_pos = [0, 1] 
# i = 2
# while i <= number: 
#     fibonacci_pos.append(fibonacci_pos[i - 1] + fibonacci_pos[i - 2])
#     i = i + 1
# #print(fibonacci_pos)

# # Отрицательный ряд Фибоначчи
# fibonacci_neg = []
# i = 0
# while i < number: 
#     fibonacci_neg.append(- fibonacci_pos[number - i])
#     i = i + 1
# #print(fibonacci_neg)

# # Требуемый ряд Негафибоначчи = Отрицательный ряд + Положительный ряд
# fibonacci = fibonacci_neg
# for i in fibonacci_pos:
#     fibonacci.append(i)

# print(fibonacci)