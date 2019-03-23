#C5: Задача FIB на Rosalind

with open ('rosalind_fib.txt') as file:
    b = file.read()
   #a = dna.split(
    a = [int(symbol) for symbol in b.split()]
   
    
    n = a[0]
    k = a[1]
    print('n', n)
    print('k', k)
    
    x = tuple()
    x = [1, 1]
    
    for i in range (2, n):
        y = x[i-1] + k*x[i-2]
        x.append(y)
        
#print( x)
print('Ответ',x[i])
