s = 'AGAACCGGGTTTGATAGTAGTCAACAGCCAACACAGGGTGGTGTCGACGATCACTCTTAAGCCCGGTTGGGATTTAGTGTGATGACAGCCGAACTATACCTGCGCCTAGAGTTAATTTAATTCTTGTGCTCAATCCTTGAAAAATTGCACTGGGATTTTACCGCGTCAAGGTACATAGTAGGTACCTAATAAAACTACGTCACTCCCATTAGTATTAAGCCCTTACACTGGATAATCACTCCTATCTCCGCAGCAAGAAGTCCATGCTACCTAAAGCGTAGCCCTCGCGATAGGGCTTGCGGCGTAACCAAACAGGCCCCAGCATTCGGTGTTCTATTAGCGCTCGTAGAAGCTCATAGAAACCTCGCGCACCCAGAGTGAGCTGCTGATGCCCATCGGCAGCTTATCGAACGTTCGTCATTGATGACCCAGTGGTGCTTCATTGTCGCAGTCTGTACGTATTACACCATGCTTTCTAGCGGGGTTTTTGCTAAAAGTTTTTTGTTTTGGACCTATTCTCGATCTGCATCCACCTCCATTGTCGACAGGGTGGAGGTTTGGAGTAGGCCGTGCAGACAAGGAGCCACCCAATGTAGGGCGTATTTGGGCTGTACTATCGCTCAATTTACCGTGCCGGGGAACTAATTGTACGACGCGTGGATACTTAACATTCCCCTCGCAGGTAGGCAACCTGTTCACCTTTTGTTGGGGCCCTTGTGCGGATGACTATACGAAATAATGGCAGCCTTACCTAATTGCCGGTCAGTCTTTGTCCCACCCGTGGCGCTGTAAGCCTCTATTACGCACGGCTTGACTGAGAAGGTTCTCCAGTTTTATAGCCGGGGCTATTTGCAAGAAGAACTTGCCCATGCGTTAGTCAGTAAGTGTTATGGGCCTCCCATTTTGT'
t = 'GAAATTCGGTCAGAGAATCGCGAACGCCCAAGTCAGCGAGCAGATATCACTGGACTGGAAGCCCCGACCGGACCTAGTTCGCTGACAGACACTAACTTCCGGAAACGAGAAATACCGGTATTGTAGTTATATAACCATGTAAAGTCTCCGTGTTATTTCATCGCGACGAGTTAAATGGGAGCGCCGGCATATGACAAGGTTACGCGGTAGATGAAAACTATCATACAACGGAGACTCGCTATCACACGCCCTTCTGGACTTTCAGGCTGCGTGATTAATAAGGATCTCTGCACAATTTCCGGCTTCTCCAGCCGGGTGCGAGCACAAAGTACTCTCCTATCGCAATCGGTTTCCCAGAGTGCCCTCGTAAGACCAGAGTGAGCCACTGATCAACACCGCCAGCGAATCAAATCATTTAAATTTATCGGCATTGGGTCCTTCATTGACGGAGTCTGGCCTGCTTGGACCATGCTCTCGATAGTAGCCTGCTATGATATTTTTTTGCTTTAGTCTTACGATCGCAGTGAGCGCGACACTAACGGCACCAGAGAGGAACAGCAGTGGAAAGTGTCGAGAGCAACCGCCTCATGATGGATCTCAAATTGAGGCTGCAATTTTTTCGAATTTATCCTCCCTGGTCTCGCGATGCTATCCATGAGCGTACTTAACAATCCCCGCACCGGTCTGTAAGCAATTCTCCCAATGGCGGCCATATTGTGACGAAGACTCGTCCAATTACGGACGGGTCACGGTACTGGCCGCCATGCGTATAAGCACGCAGTACCGTTCTAAACCACCATCATGGCCTGCATGAGACACTCGCCTGATTAGGGTTCTGCAAGGTCAGTATGGCAATTTCGACTTGCGGATCCGCTAGGGGCTAACGAAAAGTGACCTCTTAGACATC'

point_mutations = 0

for i in range(len(s)):
    if s[i] != t[i]:
        point_mutations += 1

print(point_mutations)
