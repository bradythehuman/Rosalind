def fasta_to_dict(path):
    dataset = {}

    with open(path, 'r') as f_obj:
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

    return dataset


def fasta_to_list(path):
    dataset = []

    with open(path, 'r') as f_obj:
        reader = f_obj.readlines()
        value = ''
        for line in reader:
            line = line.rstrip()
            if line[0] == '>':
                if value:
                    dataset.append(value)

                value = ''
            else:
                value += line
        dataset.append(value)

    return dataset
