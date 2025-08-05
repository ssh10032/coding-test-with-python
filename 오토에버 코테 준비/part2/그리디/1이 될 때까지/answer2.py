import sys

sys.stdin = open("input.txt", "r")

n, k = map(int, sys.stdin.readline().rstrip().split())
result = 0

while True:
    target = (n//k) * k
    result += (n-target)
    n = target

    if n<k:
        break
    result+=1
    n//=k
result+=(n-1)
print(result)