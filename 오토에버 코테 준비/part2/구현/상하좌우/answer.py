import sys

sys.stdin = open("input.txt", "r")

n = int(sys.stdin.readline().rstrip())
x, y = 1, 1
moveSet = list(map(str, sys.stdin.readline().rstrip().split()))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_type = ['L', 'R', 'U', 'D']

for move in moveSet:
    for i in range(len(move_type)):
        if move == move_type[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or nx > n or ny <1 or ny > n:
        continue
    x, y = nx, ny

print(x, y)
