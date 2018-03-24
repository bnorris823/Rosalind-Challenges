DNA = "ACGCACCTCAAAGGTGCTAATGCTTAGTCTGACGTGTGGATAAAACTGTATACAGTTTGTTGTCAATCGACCATCATATAGAATGGTGCGTCTACGCCCTCGATCATATCGACACGCGTTATATGGCAGCACTATACGTACAGACATCGTCAATTACAAGCATCAGTGTAGGGTGATACACGGTGCAAACAGGGCGTCTCTGGCCGTGACCTTCAAAACACTGGGATCGTTAACACGTAAAGTTTTCCAATCCAGGCATTGTGACATTTTTTCTTGAGGTACGAGTCAAGGGTGTTTAGCCGCATACCGGCGACCAAGGGACTGTACGTCTCTAGTATGTACGCAGATAAAGCGCTTTAGAGTGAAGACAAGAGGTTACCACCAACTGTACCAGCACGTTCTCCCGCAACACTTTGTGCGGACCCCTGTAAAGAAAATGCGGGTCGACCAGCCCGTCGTAAGGTTAAACAGCCAATTTCGTGGACGAAGCTTCTAACGAGGTATACGGAATGCCGGATCGGAGTAGAGCATTCCATCAGACGTGTGAGTTACCGAAAACTGATCGAATGAGTGGACTTATTGGACTTAAGGTTCTACGTGATCCCTCATACAGTTTTAAAAGGCCACTTTGCTAACGGTATCTGGACTTACGGCCCAGAACTCACGGCGGTACTCAGTGAGTAGCTCTATATGGACTATAGCGACCTTAAACGCTTCGTATTTCTTGGGTTCAAGCTGTATACACCCTGAACTTGCTACTTCAACCGAGGATTAAACAACAAACTTGCGCCGGGCGTGATTCTTGTTAGCATCGCCGCTCAGGTGTAACCCTTTGTGGTCAAAAAACGACCCGGTGGTCTACTCTTGTTAAAATATCGCACATCTC"
A = 0
T = 0
C = 0
G = 0
for n in DNA:
    if n == 'A':
        A += 1
    elif n == 'T':
        T += 1
    elif n == 'C':
        C += 1
    elif n == 'G':
        G += 1
    else:
        print('This is not a DNA sequence')
        break

print(str(A) + ' ' + str(C) + ' ' + str(G) + ' ' + str(T))
