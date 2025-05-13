import sys
from collections import deque
sys.stdin = open("input.txt", "r")

n, m = map(int, sys.stdin.readline().rstrip().split())

graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
data = []
target_s, target_x, target_y = map(int, sys.stdin.readline().rstrip().split())

print(graph)

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# def virus(v, x, y):
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if nx>=0 and nx<n and ny>=0 and ny<m:
#             if graph[nx][ny]==0:
#                 graph[nx][ny] = v
# q = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j]!=0:
            data.append((graph[i][j], 0, i, j))

data.sort()
q = deque(data)
print(q)

while q:
    virus, s, x, y = q.popleft()
    if s == target_s:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx and nx<n and 0<=ny and ny<m:
            if graph[nx][ny]==0:
                graph[nx][ny]=virus
                q.append((virus, s+1, nx, ny))

print(graph)
print(graph[target_x-1][target_y-1])