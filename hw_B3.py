#B3
with open ('rosalind_hamm.txt') as ss:
        ss = ss.read()
        #print(ss)
        n = int(len(ss)/2)
        #print(n)
        s = ss[0:n]
        #print(s)
        t = ss[(n):2*n]
        #print(t)
        
        d = 0
        for i in range (0,n):
             if s[i] != t[i]:
                d += 1
print(d)

          
