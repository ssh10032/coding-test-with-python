import sys
from collections import deque

# 🔹 BFS에서 최단 경로가 보장되는 이유
# 📌 BFS는 동일한 깊이(Depth)의 노드를 먼저 탐색하고, 그 다음 깊이로 이동합니다.
# 📌 즉, BFS에서 특정 노드에 도착한 "첫 번째 경로"가 항상 최단 경로가 됩니다.
#
# 🔸 BFS 탐색 구조
# 시작 노드에서 1칸 이동할 수 있는 모든 노드를 먼저 탐색.
# 그 다음, 2칸 이동할 수 있는 모든 노드 탐색.
# 이후 3칸, 4칸... 점점 확장하면서 탐색을 진행.
# 특정 노드에 가장 먼저 도착한 순간이 최단 거리임이 보장됨.

sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())



graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

print(graph)

def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >=n or ny < 0 or ny>=m:
                continue
            if graph[nx][ny]==0:
                continue
            # 처음 방문하는 경우(값이 1일 경우)에만 값을 새로 갱신
            #
            if graph[nx][ny]==1:
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx, ny))

    return graph[n-1][m-1]

print(bfs(0,0))
