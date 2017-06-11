import FASTA_Parsing

dataset = FASTA_Parsing.fasta_to_list(r'Finding_a_Shared_Motif_-_FASTA.txt')
dataset0_len = len(dataset[0])
shared_motifs = []

for start in range(dataset0_len):
    for end in range(start+1, dataset0_len+1):
        substring = dataset[0][start:end]
        if substring not in shared_motifs:
            shared = True
            for dna_string in dataset:
                if substring not in dna_string:
                    shared = False
            if shared:
                shared_motifs.append(substring)

shared_motifs.sort(key=len)
print(shared_motifs[-1])
