# Пример применения lambda, map, filter (Задача - вывести список квадратов четных чисел из заданного списка)
num = 10
squared_evens = list(map(lambda n: n ** 2, filter(lambda n: n % 2 == 0, range(num))))
print(squared_evens)
