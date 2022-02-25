# 2. Создать текстовый файл (не программно), сохранить в нём
# несколько строк, выполнить подсчёт строк и слов в каждой строке.

my_f = open("inp5_2.txt", "r", encoding='utf-8')

lines = 0
words = []

for line in my_f:
    lines += 1
    words.append(len(line.split()))

print(f'\nКоличество строк - {lines}')
print(f'\nКоличество слов в строках - {words}')

my_f.close()
