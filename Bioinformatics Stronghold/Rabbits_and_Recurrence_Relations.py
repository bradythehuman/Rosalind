n = 33
k = 4

series = [0, 1]

while len(series) - 1 < n:
    series.append(series[-1] + k*series[-2])

print(series[-1])
