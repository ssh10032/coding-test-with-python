import sys
from collections import deque



sys.stdin = open("input.txt", "r")
INF = int(1e9)
# 1~N번 도시, M개의 단방향 도로, 모든 도로의 거리는 1
# 특정 도시 X 출발, 최단 거리가 K인 모든 도시 번호 출력하는 프로그램 작성

n, m, k, x = map(int, sys.stdin.readline().rstrip().split())

graph = [[] for _ in range(n+1)]
distance = [0] * (n+1)
visited = [False] * (n+1)
print(graph)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)

print(graph)

def bfs(graph, start, visited, distance):
    queue = deque([start])
    visited[start]=True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True
                distance[i] = distance[v]+1
    return distance

result = bfs(graph, x, visited, distance)

for i in range(len(result)):
    if result[i]==k:
        print(i)
