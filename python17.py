# Задать список из N элементов, заполненных числами из [-N, N]. 
# Найти произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число
file = ('file.txt')
num = int(input('Choose a number for n: '))
for i in range(-num, num + 1):
    data = open(file, 'a')
    data.write(f"{i}\n")
    data.close()
for j in range(-num, num + 1):
    sum = sum + int(j)
data = open(file, "r")
print(sum)
