output = ''

with open('Working with Files - Dataset.txt', 'r') as f_obj:
    reader = f_obj.readlines()
    for n in range(len(reader)):
        if n % 2 != 0:
            output += reader[n]

print(output)
