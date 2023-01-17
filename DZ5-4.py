#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных
string = input('Введите строку, которую необходимо сжать:')
count = 1
for i in range(len(string) - 1):
    if i <= len(string):
        if string[i] == string[i + 1]:
            count += 1
        else:
            a = string[i]
            print(count, string[i])
            cout = 1
print(count, string[i])