import sys
from collections import deque

sys.stdin = open("input.txt", "r")

n, m = map(int, sys.stdin.readline().rstrip().split())

# 전체 맵 정보 리스트
graph = []
# 바이러스 정보 리스트
data = []

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))
    for j in range(n):
        if graph[i][j]!=0:
            # 바이러스 종류, 시간, x 좌표, y 좌표
            data.append((graph[i][j], 0, i, j))

print(graph)
print(data)

data.sort()

print(data)

# 우선 순위 큐 << 낮은 번호의 바이러스 먼저 증식
q = deque(data)

print(q)

target_s, target_x, target_y = map(int, sys.stdin.readline().rstrip().split())

# 바이러스 퍼지는 방향
dx = [-1, 0, 0, 1]
dy = [0, 1, 0, -1]

# BFS 알고리즘 수행
while q:
    virus, s, x, y = q.popleft()
    if s == target_s:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n:
            if graph[nx][ny]==0:
                graph[nx][ny] = virus
                q.append((virus, s+1, nx, ny))

print(graph[target_x-1][target_y-1])



