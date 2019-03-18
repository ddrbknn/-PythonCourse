import random
x = random.randint(0, 100)
print (x)
print ('Угадайте число от 0 до 100')
a = input()
if not a.isdigit():
    print('Введите число')
    quit()#выход из программы
a = int(a)
#print(type(a))
#print( a)
if a != x:
    while a != x:
        if a < x:
            print('Загаданное число больше вашего')
        elif a > x :
            print('Загаданное число меньше вашего')
        a = input()
        a = int(a)
        
print('Верно,', a)
