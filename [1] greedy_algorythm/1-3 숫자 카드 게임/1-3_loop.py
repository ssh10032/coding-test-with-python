import sys

sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())

result = 0

# 이중 반복문 사용한 풀이
for i in range(n):
    data = list(map(int, input().split()))

    min_value = 10001
    for a in data:
        min_value = min(min_value, a)

    result = max(result, min_value)

print(result)