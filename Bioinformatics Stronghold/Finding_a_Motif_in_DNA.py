dna_string = 'ACGTATGGAGACGTATGCTACGTATGAGGACGTATGACGTATGAGACCACGTATGACGTATGCACGTATGACGTATGCAACGTATGCGACACTCAACGTATGGGCAATACGTATGGGACGTATGGACGTATGGACGTATGACGTATGACCAAGACGTATGACGTATGCAGACGTATGGAAGCCAACGTATGCGACGTATGCCACGTATGGACGTATGCACGTATGATACGTATGACGTATGGGTCCACGTATGACGTATGCACGTATGACGTATGACGTATGCACGTATGACGTATGAACGTATGACGTATGACGTATGCGACGTATGAAACGTATGCGTACACGTATGGCGACGTATGACGTATGACGTATGGATATACGTATGAACGTATGCACGTATGCGAACGTATGTACGTATGAGGACACGTATGCTCACGTCACGTATGCACGTATGTACGTATGTAATGTACGTATGGAAGAGCACGTATGCCTACGTATGACGTATGATACGTATACGTATGGTCGTTACGTATGAACGTATGAAGACGTATGACGTATGTGACGTATGCCCTACGTATGCACGTATGCATTAACGTATGCACTACGTATGTACGTATGTTAACGTATGACGTATGCTAAACGTATGTACGGAGGAACGTATGGACGTATGAATTGGACGTATGACGTATGACGTATGACGTATGCCCAATACGTATGGACGTATGATATCTAACGTATGAGGCAGACGTATGCAACGTATGTCACTAACGTATGCCGGAACGTATGAACGTATGCACGTATGAACGTATGAACGTATGCGCACGTATG'
dna_motif = 'ACGTATGAC'
motif_indices = []
motif_len = len(dna_motif)

for i in range(len(dna_string) - motif_len + 1):
    if dna_string[i:i + motif_len] == dna_motif:
        motif_indices.append(i + 1)

for i in motif_indices:
    print(i, end=' ')
