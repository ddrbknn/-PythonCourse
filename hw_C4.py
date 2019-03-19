#C4
import math
print ('Введите  числа a, b, c из уравнения ax2+bx+c=0,')
xxx = input()
xx = [int(symbol) for symbol in xxx.split()]
a = xx[0]
b = xx[1]
c = xx[2]
D = b*b - 4*a*c
#print(D)
if D < 0:
    print ('Уравнение не имеет корней')
else:
    x1 = (-b + math.sqrt(D))/(2*a)
    print(x1)
    if  D > 0:
        x2 = (-b - math.sqrt(D))/(2*a)
        print(x2)
