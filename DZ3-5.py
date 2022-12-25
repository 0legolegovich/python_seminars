# Семинар 3 Задача 5
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

number = int(input('Задайте число положительных элементов последовательности: '))

# Положительный ряд Фибоначчи
fibonacci_pos = [0, 1] 
i = 2
while i <= number: 
    fibonacci_pos.append(fibonacci_pos[i - 1] + fibonacci_pos[i - 2])
    i = i + 1
#print(fibonacci_pos)

# Отрицательный ряд Фибоначчи
fibonacci_neg = []
i = 0
while i < number: 
    fibonacci_neg.append(- fibonacci_pos[number - i])
    i = i + 1
#print(fibonacci_neg)

# Требуемый ряд Негафибоначчи = Отрицательный ряд + Положительный ряд
fibonacci = fibonacci_neg
for i in fibonacci_pos:
    fibonacci.append(i)

print(fibonacci)