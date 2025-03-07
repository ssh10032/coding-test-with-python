import sys
import bisect

sys.stdin = open("input.txt", "r")

n = int(sys.stdin.readline().rstrip())
s = list(map(int, sys.stdin.readline().rstrip().split()))

s.reverse()

lis = []

for power in s:
    pos = bisect.bisect_left(lis, power)
    if pos == len(lis):
        lis.append(power)
    else:
        lis[pos] = power

print(n)
print(s)