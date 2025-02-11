import sys

sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))

    # min() 함수를 이용한 풀이
    min_value = min(data)

    result = max(min_value, result)

print(result)