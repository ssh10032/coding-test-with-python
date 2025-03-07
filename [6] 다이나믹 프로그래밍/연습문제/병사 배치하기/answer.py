import sys

sys.stdin = open("input.txt", "r")

n = int(sys.stdin.readline().rstrip())

s = list(map(int, sys.stdin.readline().rstrip().split()))

print(n)
print(s)