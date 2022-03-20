# Сообщить в какой четверти координатной плоскости или на какой оси находится точка с координатами Х и У 
coorX = int(input("Choose coordinates for x: "))
coorY = int(input("Choose coordinates for y: "))
if coorX and coorY > 0:
    print("Вы находитесь в первой четверти")
elif coorX < 0 and coorY > 0:
    print("Вы находитесь во второй четверти")
elif coorX < 0 and coorY < 0:
    print("Вы находитесь в третей четверти")
elif coorX > 0 and coorY < 0:
    print("Вы находитесь в четвертой четверти четверти")
else:
    print("Повторите попытку")