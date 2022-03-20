# Дано число обозначающее день недели. Вывести его название и указать является ли он выходным.
import random
n1 = "monday"
n2 = "tuesday"
n3 = "wednesday"
n4 = "thursday"
n5 = "friday"
n6 = "saturday"
n7 = "sunday"
num1 = random.randint(1, 8)
print(num1)
if num1 == 6:
    print(f"Wow, today is {n6} and its weekend")
elif num1 == 7:
    print(f"Wow, today is {n7} and its weekend")
elif num1 == 1:
    print(f"Wow, today is {n1}")
elif num1 == 2:
    print(f"Wow, today is {n2}")
elif num1 == 3:
    print(f"Wow, today is {n3}")
elif num1 == 4:
    print(f"Wow, today is {n4}")
else:
    print(f"Wow, today is {n5}")

