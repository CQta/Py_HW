import math
x = int(input("Введите x для 1 числа "))
y = int(input("Введите y для 1 числа "))
x2 = int(input("Введите x для 2 числа "))
y2 = int(input("Введите y для 2 числа "))
print(round(math.sqrt(((x2-x)**2)+(y2-y)**2), 3))
