# Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
numbers = [10, 20, 15, 15, 20, 30, 30, 35, 40]
unique = []
for number in numbers: 
    if number not in unique:
        unique.append(number)
print(unique)




