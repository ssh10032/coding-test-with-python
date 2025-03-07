import sys

sys.stdin = open("input.txt", "r")

n = int(sys.stdin.readline().rstrip())

# print(n)
d = []
test = []
for _ in range(n):
    n_list = list(map(int, sys.stdin.readline().rstrip().split()))
    test.append(n_list)
    # print(len(n_list))
    d.append([0] * len(n_list))

d[0][0] = test[0][0]
d[1][0] = d[0][0] + test[1][0]
d[1][1] = d[0][0] + test[1][1]

for r in range(2, n):
    for c in range(len(d[r])):
        if c == 0:
            d[r][c] = test[r][c] + d[r-1][c]
        elif c == len(d[r])-1:
            d[r][c] = test[r][c] + d[r-1][c-1]
        else:
            d[r][c] = test[r][c] + max(d[r-1][c-1], d[r-1][c])

# print(test)
# print(d)

print(max(d[n-1]))