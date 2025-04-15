import sys

sys.stdin = open("input.txt", "r")

n, m = map(int, sys.stdin.readline().rstrip().split())

result = 0

for _ in range(n):
    data = list(map(int, sys.stdin.readline().rstrip().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)
