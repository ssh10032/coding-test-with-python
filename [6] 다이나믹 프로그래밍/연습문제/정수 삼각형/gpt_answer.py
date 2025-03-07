import sys
sys.stdin = open("input.txt", "r")

n = int(sys.stdin.readline().rstrip())
tr = []

for _ in range(n):
    n_list = list(map(int, sys.stdin.readline().rstrip().split()))
    tr.append(n_list)

print(tr)

for r in range(1, n):
    for c in range(len(tr[r])):
        if c == 0:
            tr[r][c] += tr[r-1][c]
        elif c==len(tr[r])-1:
            tr[r][c] += tr[r-1][c-1]
        else:
            tr[r][c] += max(tr[r-1][c-1], tr[r-1][c])

print(tr)
print(max(tr[-1]))