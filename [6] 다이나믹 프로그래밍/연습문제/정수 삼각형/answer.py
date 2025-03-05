import sys

sys.stdin = open("input.txt", "r")

n = int(sys.stdin.readline().rstrip())

print(n)
test = []
for _ in range(n):
    n_list = list(map(int, sys.stdin.readline().rstrip().split()))
    test.append(n_list)

print(test)