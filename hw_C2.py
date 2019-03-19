#C2
print ('Введите числo')
b = input()

n = len(b)
if n == 1:
    print ('Число однозначное', 'Сумма цифр = ', b, 'Произведение  цифр вычислить нельзя (или составляет 0)')
else:
    sm = 0
    pr = 1
    for symbol in b:
        q = int(symbol)
        print(q, type(q))
        sm = sm + q
        pr = pr*q
    print('Сумма цифр = ', sm)
    print ('Произведение цифр = ', pr)
