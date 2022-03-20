# Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат
import random
x = random.randint(0,2)
y = random.randint(0,2)
z = random.randint(0,2)
print((x and y and z) == !x or !y or !Z)