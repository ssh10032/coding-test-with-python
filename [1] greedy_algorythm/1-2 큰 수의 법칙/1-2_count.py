import sys

sys.stdin = open("input.txt", "r")

n, m, k = map(int, input().split())

data = list(map(int, input().split()))

print(data)

data.sort()

first = data[n-1]
second = data[n-2]

# 가장 큰 수가 더해진 갯수 계산
# m개의 수 >> (k+1)개의 list가 반복 + 나머지 큰수들
count = m // (k+1) * k
count += m % (k+1)
print(count)

result = 0
result += (count) * first
# m - 가장 큰수 갯수 == 두 번째 큰 수 갯수
result += (m-count) * second

print(result)