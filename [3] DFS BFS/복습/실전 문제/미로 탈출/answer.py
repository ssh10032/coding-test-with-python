import sys
from collections import deque
sys.stdin = open("input.txt", "r")

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

# 처음 위치 (1, 1)
# 미로 출구 (n, m)
# 괴물이 있는 곳 0, 없는 곳 1
# 탈출하기 위한 최소 경로 길이 출력
n, m = map(int, sys.stdin.readline().rstrip().split())

# 최소 경로 문제니까
# bfs 문제 인것 같음
# deque 자료 구조 사용?
graph = []

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if graph[nx][ny]==0:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx, ny))
    return graph[n-1][m-1]

print(bfs(0,0))

visited = [[0] * m for _ in range(n)]