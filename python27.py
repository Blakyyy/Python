# Строка содержит набор чисел. Показать большее и меньшее число
import random
list = [random.randint(1, 101),random.randint(1, 101), random.randint(1, 101), random.randint(1, 101) ]
listlenght = len(list)
max = 0
min = list[0]
for i in range(listlenght):
    if list[i] > max:
        max = list[i]

for i in range(listlenght):
    if list[i] < min:
        min = list[i]

print(list)
print(max)
print(min)    


    
