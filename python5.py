# Дано число. Проверить кратно ли оно 5 и 10 или 15 но не 30
number = int(input("Insert your number: "))
if number % 5 == 0 and number % 10 == 0:
    print(f"Число {number} кратно 5 и 10")
elif number % 15 == 0 and number % 30 != 0:
    print(f"Число {number} кратно 15, но не 30")
else:
    print("Число не выполняет ни одного из условий")

