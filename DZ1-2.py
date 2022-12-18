# Семинар 1 Задача 2:
#Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
print("Проверка истинности выражения: ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z")
x = 0
y = 0
z = 0
for x in range (0, 2):
    for y in range (0, 2):
        for z in range (0, 2):
             print("x = " + str(x) + ", y = " + str(y) + ", z = " + str(z), end=" | ")
             result1 = not (x or y or z)
             result2 = not x and not y and not z
             print("expression1 = " + str(result1) + ", expression2 = " + str(result2), end=" | ")
             if result1 == result2:
                    print("Выражения равны")
