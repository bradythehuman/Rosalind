n = 0
p = ''  # permutation

with open(r'Longest_Increasing_Subsequence_-_Dataset.txt', 'r') as f_obj:
    reader = f_obj.readlines()
    n = int(reader[0])
    for line in reader[1:]:
        p += line
    p = ''.join(p.split())

ip = ['', '1']  # increasing permutations
dp = ['', str(n)]  # decreasing permutations


def expand_permutations(plist, add):
    temp = []
    for permutation in plist:
        temp.append(permutation)
        temp.append(permutation + str(add))
    return temp[:]


def find_longest(plist):
    for permutation in plist:
        plen = len(permutation)
        i = 0
        for number in p:
            if permutation[i] == number:
                i += 1
            if i == plen:
                return permutation


def format_print(permutation):
    for number in permutation:
        print(number, end=' ')
    print()

for num in range(2, n+1):
    ip = expand_permutations(ip, num)

for num in range(1-n, 0):
    num = -num
    dp = expand_permutations(dp, num)

ip.sort(key=len, reverse=True)
dp.sort(key=len, reverse=True)

li = find_longest(ip)  # longest increasing
ld = find_longest(dp)  # longest decreasing

format_print(li)
format_print(ld)
