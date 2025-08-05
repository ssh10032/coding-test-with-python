import sys

sys.stdin = open("input.txt", "r")

n = int(sys.stdin.readline().rstrip())

print(n)

count = 0

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count+=1

print(count)