import sys

sys.stdin = open("input.txt", "r")

n = int(sys.stdin.readline().rstrip())

array = list(map(int, sys.stdin.readline().rstrip().split()))

array.sort()


target = 1
for i in array:
    if i > target:
        break
    else:
        target+=i

print(target)