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

print(reverse_pattern("AGT"))
print(reverse_pattern("AGTCGCATAGT"))