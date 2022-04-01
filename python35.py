# В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, чтобы выполнялось 
# условие A[i] - 1 = A[i-1]. Найти его.
import random
data = 'condition.txt'
data_list = []
k = random.randint(1, 101)
with open ('condition.txt', 'w' ) as data:
    for j in range(1, 101):
        if j == k:
            j += 1
        data.write(f' {j} ')
with open("condition.txt") as data:
    data_list = [int(x) for x in data.read().split()]
print(data_list)
for i in range(len(data_list)):
    if i == 0:
        i += 1
    if data_list[i] - 1 != data_list[i-1]:
        i += 1 
        print(i)
        break


        

