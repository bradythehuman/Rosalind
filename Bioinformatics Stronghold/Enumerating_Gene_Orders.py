n = 7  # Only input variable (number of number to permutate)
r = range(1, n+1)
p_total = 1
pl_stable = []  # pl = permutations list

for i in r:
    p_total *= i
    pl_stable.append([i])

p_len = 1


def add_len(pl):
    pl_temp = []

    for line in pl:
        for j in r:
            p = line[:]
            if j not in line:
                p.append(j)
                pl_temp.append(p)

    return pl_temp[:]

while p_len < n:
    pl_stable = add_len(pl_stable)
    p_len += 1

print(p_total)
for ln in pl_stable:
    for num in ln:
        print(num, end=' ')
    print()
