import sys

sys.stdin = open("input.txt", "r")

n, m, k = map(int, sys.stdin.readline().rstrip().split())

data = list(map(int, sys.stdin.readline().rstrip().split()))

data.sort()
first = data[-1]
second = data[-2]

result = 0
while True:
    for i in range(k):
        if m==0:
            break
        result+=first
        m-=1
    if m==0:
        break
    result+=second
    m-=1

print(result)
