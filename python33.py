# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен 
import random
num = random.randint(0, 101)
k = int(input('Введите натуральную степень для k: '))

data = 'polinomio.txt'
for i in range(k, k - k, -1):
    num = random.randint(0, 101)
    with open ('polinomio.txt', 'a') as data:
        if i == 1:
            data.write(f'{num}')
            data.write('x=0')
            break
        data.write(f'{num}x^{i}+')
        
            

        
        
        
