# Реализовать алгоритм перемешивания списка. 
import random
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listlength = len(list)
for i in range(listlength):
    numrand = random.randint(i, listlength - 1)
    numero = list.pop(numrand)
    list.append(numero)
print(list)