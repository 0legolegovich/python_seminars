# Семинар 1 Задача 3:
#Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

print("Нумерация четвертей координатной плоскости:")
print("2 | 1")
print("-----")
print("3 | 4")

x = float(input("Введите значение координаты X: "))
y = float(input("Введите значение координаты Y: "))

if (x==0 and y==0):
    print ("Введенная точка находится на пересечении осей X и Y")
elif (x==0):
    print("Введенная точка находится на оси X")
elif (y==0):
    print("Введенная точка находится на оси Y")
elif (x>0 and y>0):
    print("Введенная точка находится в первой четверти")
elif (x<0 and y>0):
    print("Введенная точка находится во второй четверти")
elif (x<0 and y<0):
    print("Введенная точка находится в третьей четверти")
elif (x>0 and y<0):
    print("Введенная точка находится в четвертой четверти")
