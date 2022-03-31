# Строка содержит набор чисел. Показать большее и меньшее число
num = (input('Insert numbers with space beetween them: ').split())
list = []
for i in range(0, len(num)):
    list.append(int(num[i]))
print(list)
print(max(list))
print(min(list))




    
