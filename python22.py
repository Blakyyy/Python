# Найти сумму чисел списка стоящих на нечетной позиции
list = (input('Введите числа через пробел: ')).split(" ")
count = 0
newlist = [int(i) for i in list]
for j in range(0, len(newlist)):
    if j % 2 != 0:
        count = count + newlist[j]
print(newlist)
print(count)