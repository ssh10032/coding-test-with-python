import sys

sys.stdin = open("input2.txt", "r")

n, m = map(int, sys.stdin.readline().rstrip().split())

result = 0
for i in range(n):
    data = list(map(int, sys.stdin.readline().rstrip().split()))

    min_value = 10001

    for a in data:
        min_value = min(min_value, a)

    result = max(result, min_value)

print(result)

