# По двум заданным числам проверить является ли одно квадратом второго 
import random
number1 = random.randint(1, 11)
number2 = random.randint(1, 101)
if number1 * number1 == number2:
    print(f" Второй номер({number2}) является квадратом первого номера ({number1})")
else:
    print(f" Второй номер({number2}) НЕ является квадратом первого номера ({number1})")