#SUBS
with open ('rosalind_subs.txt') as file:
    dna = file.read()
    a = dna.split()
   #print (type(a), a)
    b = a[0]
    c = a[1]
    n = len(b)
    l = len(c)
    x = tuple()
    x = []
    for i in range (0, n-l+1):
        if b[i:i+l]== c:
            #print(i)
            x.append(i)
print(x)
        
