import sys

sys.stdin = open("input.txt", "r")

n = int(sys.stdin.readline().rstrip())

print(n)

array = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

print(array)

array = sorted(array, reverse=True)

for i in array:
    print(i, end=' ')