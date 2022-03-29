# Задать список из n чисел последовательности (1+1n)n и вывести на экран их сумму
n = int(input('Choose a number for N: '))
list = []
for i in range(1, n + 1):
    list.append((1 +1 * i ) * i)
slist = sum(list)
print(list)
print(slist)
