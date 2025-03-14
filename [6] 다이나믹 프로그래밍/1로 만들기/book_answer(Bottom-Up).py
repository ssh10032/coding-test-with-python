import sys

# answer
# input 1: 1
sys.stdin = open("input.txt", "r")

n = int(sys.stdin.readline().rstrip())
print(n)
d = [0] * 30001

for i in range(2, n+1):
    d[i] = d[i-1]+1
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2]+1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3]+1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i//5]+1)

print(d[n])
