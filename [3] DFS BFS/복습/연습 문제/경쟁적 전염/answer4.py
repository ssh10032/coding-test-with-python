import sys
from collections import deque
# n*n 크기의 시험관
# 바이러스 종류 1~K까지 있음
# 1초마다 상하좌우로 번식, 번호가 낮은 바이러스부터 번식
# s초가 지난 후에 (x, y)에 존재하는 바이러스 종류를 출력

# 우선순위가 있으면 queue로 접근하는걸 먼저 생각해보자
sys.stdin = open("input2.txt", "r")

n, k = map(int, sys.stdin.readline().rstrip().split())

graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
data = []

target_s, target_x, target_y = map(int, sys.stdin.readline().rstrip().split())

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for i in range(n):
    for j in range(n):
        if graph[i][j]!=0:
            data.append((graph[i][j], 0, i, j))

print(data)
data.sort()
print(data)
q = deque(data)
print(q)

while q:
    virus, s, x, y = q.popleft()

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx and nx<n and 0<=ny and ny<n:
            if graph[nx][ny]==0:
                graph[nx][ny]=virus
                q.append((virus, s+1, nx, ny))

    if s+1==target_s:
        break

print(graph[target_x-1][target_y-1])



