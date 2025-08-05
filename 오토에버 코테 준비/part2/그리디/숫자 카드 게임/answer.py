import sys

sys.stdin = open("input.txt", "r")
# sys.stdin = open("input.txt", "r")

# 행렬의 행 n  열 m
n, m = map(int, sys.stdin.readline().rstrip().split())

result = 0

for i in range(n):
    data = list(map(int, sys.stdin.readline().rstrip().split()))
    min_value = min(data)

    result = max(result, min_value)

print(result)