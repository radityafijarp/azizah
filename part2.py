def reverse_pattern(pattern):
    dnaPair=""

    for i in pattern:
        if i == "A":
            base="T"
        elif i == "T":
            base="A"
        elif i == "G":
            base="C"
        elif i == "C":
            base = "G"
        
        dnaPair=base+dnaPair
    return dnaPair

def count_k_mer(genome,pattern):
    reverse_complement=reverse_pattern(pattern)
    count_k=0

    for i in range(len(genome)-len(pattern)+1):
        combination=genome[i:i+len(pattern)]
        if combination == reverse_complement or combination ==pattern:
            count_k=count_k+1
    return count_k

print(count_k_mer('ACAACTATGCATACTATCGGGAACTATCCTATAGT', 'ACTAT'))
print( count_k_mer('CGATATATCCATAG', 'ATA'))

