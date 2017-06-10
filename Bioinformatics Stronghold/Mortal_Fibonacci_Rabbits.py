n = 88
m = 19

series = [1]
while n-1:
    a = 0
    for i in series[1:]:
        a += i
    if len(series) < m:
        series = [a] + series
    else:
        series = [a] + series[:-1]
    n -= 1

result = 0
for i in series:
    result += i
print(result)
