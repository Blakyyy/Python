# В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов
import math
list = [2.1, 4.2, 1.6, 8.2, 9.7, 3.5]
max = 0
for i in range(0, len(list)):
    x = math.modf(list[i])
    if x[0] > max:
        max = x[0]
min = max
for j in range(0, len(list)):
    x1 = math.modf(list[j])
    if x1[0] < min:
        min = x1[0]
diff = max - min
print(list)
print(max)
print(min)
print(diff)