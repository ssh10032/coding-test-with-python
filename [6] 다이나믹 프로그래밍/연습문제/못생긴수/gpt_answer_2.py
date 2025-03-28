import sys

sys.stdin = open("input.txt", "r")

n = int(sys.stdin.readline().rstrip())

print(n)

d = [1]
num_list = [2, 3, 5]

idx = 0
while len(d) < n:
    current = d[idx]
    for num in num_list:
        candidate = current * num
        if candidate not in d:
            d.append(candidate)
    idx += 1
    d.sort()
print(d[n-1])