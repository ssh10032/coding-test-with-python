import heapq
import sys

sys.stdin = open("input.txt", "r")

n, m = map(int, sys.stdin.readline().rstrip().split())
start = int(sys.stdin.readline().rstrip())
INF = int(1e9)

# 연결 정보 리스트
graph = [[] for i in range(n+1)]
# 최단 거리 테이블 초기화
distance = [INF] * (n+1)


for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
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
    if distance[i]==INF:
        print("infinity")
    else:
        print(distance[i])
