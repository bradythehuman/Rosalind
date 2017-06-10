codon_dict = {}

with open('Translating RNA into Protein - RNA codon table.txt', 'r') as f_obj:
    reader = f_obj.readlines()
    for line in reader:
        line = line.strip()
        codon_list = line.split(' ')
        codon_dict[codon_list[0]] = codon_list[1]

dataset_str = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'
dataset_list = []

while dataset_str:
    dataset_list.append(dataset_str[0:3])
    dataset_str = dataset_str[3:]

output = ''

for codon in dataset_list:
    if codon_dict[codon] != 'Stop':
        output += codon_dict[codon]

print(output)
