#Найти произведение пар чисел в списке. Парой считаем первый и последний элемент
list = [3, 10, 4, 2, 7, 5]
print(list)
lengthFI = round(len(list)/2)
for i in range(0, lengthFI):
    result = list[i] * list[(len(list) - 1) - i]
    print(result)
