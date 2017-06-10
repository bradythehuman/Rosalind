dataset = {}

with open('Computing GC Content - Dataset.txt', 'r') as f_obj:
    reader = f_obj.readlines()
    key = ''
    value = ''
    for line in reader:
        if line[0] == '>':
            if key:
                dataset[key] = value
            key = line[1:].rstrip()
            value = ''
        else:
            value += line.rstrip()
    dataset[key] = value

cg_content = {}

for key in dataset:
    at = 0
    cg = 0
    for nt in dataset[key]:
        if nt == 'A' or nt == 'T':
            at += 1
        if nt == 'C' or nt == 'G':
            cg += 1
    cg_content[key] = 100 * cg / (at+cg)

high = ''

for key in cg_content:
    if high == '':
        high = key
    elif cg_content[key] > cg_content[high]:
        high = key
    results = [high, cg_content[high]]

print(str(results[0]) + '\n' + str(results[1]))
