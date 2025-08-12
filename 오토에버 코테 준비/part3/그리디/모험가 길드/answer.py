import sys

sys.stdin = open("input.txt", "r")

n = int(sys.stdin.readline().rstrip())

array = list(map(int, sys.stdin.readline().rstrip().split()))

array.sort()

result = 0

n = 1

for i in array:
    if n>=i:
        result+=1
        n=1
    else:
        n+=1

print(result)