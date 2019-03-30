import math
from math import sin, cos, ceil, floor

print ('Вычисление интеграла функции y = sin(x)')
print ('Введите границы интервала интегрирования (2 числа)')
b = input()
a = [float(symbol) for symbol in b.split()]
x1 = a[0]
x2 = a[1]
H = (x2-x1)/(100*(x2-x1+2))#весы
y1 = abs(sin(x1)*H)
y2 = abs(sin(x2)*H)
S = y1 + y2

#for x in range (ceil(x1), floor(x2)):
#for x in range (x1, x2, 0.):
x = x1
while x < x2:
    x = x + 0.01
    y = abs(sin(x)*H)
    S = S + y
print ('Методом прямоугольнико      ',S)

y11 = -cos(x1)
y22 = -cos(x2)
Sa = y22 - y11
print ('Аналитически    ',Sa)
