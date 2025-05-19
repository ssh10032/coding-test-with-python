import sys
from collections import deque

# 모든 간선의 비용이 1일 때는, 너비 우선 탐색을 이용해서 최단 거리를 찾을 수 있음
sys.stdin = open("input.txt", "r")

n, m, k, x = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)

# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * (n+1)
distance[x] = 0

q = deque([x])
while q:
    now = q.popleft()
    for next_node in graph[now]:
        if distance[next_node]==-1:
            distance[next_node]=distance[now]+1
            q.append(next_node)

check = False
for i in range(1, n+1):
    if distance[i]==k:
        print(i)
        check = True
if check==False:
    print(-1)
