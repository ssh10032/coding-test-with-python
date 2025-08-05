import sys

sys.stdin = open("input.txt", "r")
# 정사각형 맵 행렬 크기 정보 n * n
# 시작 좌표는  (1, 1) 최우측 하단 좌표는 (n, n)
n = int(sys.stdin.readline().rstrip())

moveset = list(map(str, sys.stdin.readline().rstrip().split()))
x, y = 0, 0
print(n)
print(moveset)

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for dir in moveset:
    if dir == 'U':
        nx = x - 1
        ny = y
    elif dir == 'D':
        nx = x + 1
        ny = y
    elif dir == 'R':
        nx = x
        ny = y + 1
    else:
        nx = x
        ny = y - 1
    if nx>=0 and nx < n and ny>=0 and ny<n:
        x = nx
        y = ny

print(x+1)
print(y+1)