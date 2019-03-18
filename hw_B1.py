with open ('rosalind_rna.txt') as file:
    dna = file.read()
    print(dna)
    rna = dna.replace('T','U')
    print(rna)
    
        
