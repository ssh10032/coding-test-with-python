import sys
from collections import deque

sys.stdin = open("input.txt", "r")

# 도시 수 n, 도로 개수 m, 최단거리 k, 출발 도시 x
n, m, k, x = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)

# 도시 간 거리 초기화
distance = [-1] * (n+1)
distance[x]=0

# 큐는 선입선출
q = deque([x])

while q:
    now = q.popleft()

    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node]=distance[now]+1
            q.append(next_node)

check = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True
if check == False:
    print(-1)



