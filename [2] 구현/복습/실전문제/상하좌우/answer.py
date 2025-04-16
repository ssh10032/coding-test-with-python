import sys

sys.stdin = open("input.txt", "r")

n = int(sys.stdin.readline().rstrip())

x, y = 1, 1

str_list = map(str, sys.stdin.readline().rstrip().split())

for i in str_list:
    if i == "R":
        if 0<y+1<=n:
            y+=1
    elif i=="L":
        if 0<y-1<=n:
            y-=1
    elif i=="U":
        if 0<x-1<=n:
            x-=1
    elif i=="D":
        if 0<x+1<=n:
            x+=1

print(x, end=" ")
print(y)
