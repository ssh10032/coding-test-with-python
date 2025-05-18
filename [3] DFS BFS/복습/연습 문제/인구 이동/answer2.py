import sys
from collections import deque

sys.stdin = open("input.txt", "r")

# 인구 수 차이가 l명 이상 r명 이하면 인구 이동이 일어남
n, l, r = map(int, sys.stdin.readline().rstrip().split())

union = [[-1] * n for _ in range(n)]
graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

print(graph)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

q = deque((graph[0][0], 0, 0))
# union[0][0]=0
union_c = 0

print(q)
count = 0
while q:
    p, x, y = q.popleft()
    union[x][y]=union_c
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx>=0 and nx<n and ny>=0 and ny<n:
            if l<=abs(graph[nx][ny]-graph[x][y]) and abs(graph[nx][ny]-graph[x][y])<=r and union[nx][ny]==-1:
                union[nx][ny]=union[x][y]
                q.append((graph[nx][ny], nx, ny))