# Найти максимальное из пяти чисел
import random
list = [random.randint(1, 101), random.randint(1, 101), random.randint(1, 101), random.randint(1, 101), random.randint(1, 101) ]
max = 0
length = len(list)
for i in range(length - 1):
    if list[i] > max:
        max = list[i]
print(list)
print(max)