# Написать программу преобразования десятичного числа в двоичное
num = int(input("Choose a number to convert: "))
def DecimalToBinary(num):
        if num >= 1:
            DecimalToBinary(num // 2)
            print (num % 2) 
DecimalToBinary(num)