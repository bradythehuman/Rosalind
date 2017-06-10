homologous_strands = []

with open('Consensus and Profile - FASTA.txt', 'r') as f_obj:
    reader = f_obj.readlines()
    strand = ''
    for line in reader:
        if line[0] == '>':
            if strand:
                homologous_strands.append(strand)
            strand = ''
        else:
            strand += line.rstrip()
    homologous_strands.append(strand)

strand_len = len(homologous_strands[0])
profile = {'A': [0]*strand_len, 'C': [0]*strand_len, 'G': [0]*strand_len, 'T': [0]*strand_len}

bases = ['A', 'C', 'G', 'T']
consensus = ''

for i in range(strand_len):
    for strand in homologous_strands:
        profile[strand[i]][i] += 1
    base_counts = [profile['A'][i], profile['C'][i], profile['G'][i], profile['T'][i]]
    max_count = max(base_counts)
    max_index = base_counts.index(max_count)
    consensus += bases[max_index]

print(consensus)
for base in bases:
    print(base + ':', end=' ')
    for base_count in profile[base]:
        print(base_count, end=' ')
    print()
