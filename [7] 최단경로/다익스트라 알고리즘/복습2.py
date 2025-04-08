import sys
import heapq

sys.stdin = open("input.txt", "r")

INF = int(1e9)
# 노드, 간선 수 기록
n, m = map(int, sys.stdin.readline().rstrip().split())
# 시작점
start = int(sys.stdin.readline().rstrip())

graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)


for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append((b, c))

print(graph)

def dijkstra(start):
    q = []
    distance[start] = 0

    # 우선 순위 큐의
    # 첫번째 요소가 비용!!!
    # 두번째 요소가 노드번호
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now]<dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("infinity")
    else:
        print(distance[i])