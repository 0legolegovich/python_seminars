# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв"

my_str = 'абв Какой-то очень АБв важный АБВ текст абв'
new_str = list(filter(lambda elem: 'абв' not in elem.lower(), my_str.split()))
print(*new_str)