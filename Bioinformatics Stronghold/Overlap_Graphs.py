dataset = {}

with open('Overlap Graphs - FASTA.txt', 'r') as f_obj:
    reader = f_obj.readlines()
    value = ''
    for line in reader:
        line = line.rstrip()
        if line[0] == '>':
            if value:
                dataset[key] = value
            key = line[1:]
            value = ''
        else:
            value += line
    dataset[key] = value

k = 3
adjacency_list = []

for key1 in dataset:
    s1 = dataset[key1][-k:]
    for key2 in dataset:
        if key1 != key2:
            s2 = dataset[key2][:k]
            if s1 == s2 and dataset[key1] != dataset[key2]:
                adjacency_list.append((key1, key2))

for edge in adjacency_list:
    print(edge[0] + ' ' + edge[1])
