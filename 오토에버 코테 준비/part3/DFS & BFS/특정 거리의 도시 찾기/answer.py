import sys
from collections import deque

sys.stdin = open("input.txt", "r")

# n 도시 개수, m 도로 개수, # 거리 정보 k, 출발 도시 번호 x
n, m, k, x = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)

distance = [-1] * (n+1)
distance[x]=0

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