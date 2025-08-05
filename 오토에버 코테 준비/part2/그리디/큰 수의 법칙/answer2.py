import sys

sys.stdin = open("input.txt", "r")

n, m, k = map(int, sys.stdin.readline().rstrip().split())

data = list(map(int, sys.stdin.readline().rstrip().split()))

data.sort()
first = data[n-1]
second = data[n-2]

# count는 가장 큰 수의 갯수
count = int(m/(k+1)) * k
count += m % (k+1)

result = 0
result += count * first
result += (m-count) * second

print(result)
