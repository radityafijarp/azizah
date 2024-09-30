#Part 1
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

# Part 2
def count_k_mer(genome,pattern):
    reverse_complement=reverse_pattern(pattern)
    count_k=0

    for i in range(len(genome)-len(pattern)+1):
        combination=genome[i:i+len(pattern)]
        if combination == reverse_complement or combination ==pattern:
            count_k=count_k+1
    return count_k

# Part 3
def frequent_k_mer(genome, k):
    k_mer_count = {}
    result = []
    max_count = 0

    # Step 1: Count each k-mer in the genome
    for i in range(len(genome) - k + 1):
        k_mer = genome[i:i+k]
        if not k_mer in k_mer_count:
            k_mer_count[k_mer] = count_k_mer(genome,genome[i:i+k])
        
        # Update max count dynamically
        if k_mer_count[k_mer] > max_count:
            max_count = k_mer_count[k_mer]

    # Step 2: Collect all k-mers with the maximum count
    for k_mer, count in k_mer_count.items():
        if count == max_count:
            result.append(k_mer)
    
    return result


def main():
    genome_file = input("Genome file name: ")
    
    try:
        with open(genome_file, 'r') as f:
            genome = f.read().strip()
    except FileNotFoundError:
        print("File not found.")
        return
    
    while True:
        print("\nChoose an option:")
        print("[1] Compute a reverse complement of a k-mer pattern")
        print("[2] Count a k-mer pattern")
        print("[3] Find most frequent k-mer patterns")
        print("[0] Exit")
        
        choice = input("Select an operation [1/2/3/0]: ")
        
        if choice == '1':
            pattern = input("Input your pattern: ")
            rev_comp = reverse_pattern(pattern)
            print(rev_comp)
        elif choice == '2':
            pattern = input("Input your pattern: ")
            count = count_k_mer(genome, pattern)
            print(count)
        elif choice == '3':
            k = int(input("Input your value of k: "))
            most_frequent_kmers = frequent_k_mer(genome, k)
            for kmer in most_frequent_kmers:
                print(kmer)
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

# Menjalankan program
if __name__ == "__main__":
    main()