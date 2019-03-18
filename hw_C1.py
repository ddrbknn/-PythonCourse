print ('Введите список чисел')
b = input()
a = [int(symbol) for symbol in b.split()]
print(a)
n = len(a)
print (n)
b = list()
b = []
for i  in range (1, n):
    if a[i] > a[i-1]:
        b.append(a[i])
print(b)
        
    
        
    
