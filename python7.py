# Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат
x = False
y = True
Z = False

for x in range(2):
    for y in range(2):
        for Z in range(2):
            r1 = not (x or y or Z)
            r2 = not x and not y and not Z
            

if r1 == r2:
    print("True, Ley de Morgan ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z")
else:
    print("False, ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z")
