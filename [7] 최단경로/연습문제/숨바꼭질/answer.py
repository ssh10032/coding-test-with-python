import sys
import heapq
sys.stdin = open("input.txt", "r")

# n개의 헛간 개수, m개의 양방향 통로 개수
n, m = map(int, sys.stdin.readline().rstrip().split())

INF = int(1e9)

# 각 헛간에 연결되어있는 통로에 대한 정보를 담는 리스트 만들기
graph = [[] for _ in range(n+1)]

# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

def dijkstra(start):
    q = []

    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(1)

max_dist = max(distance[1:])
count = 0
for i in range(len(distance)):
    if distance[i] == max_dist:
        if count == 0:
            print(i)
        count+=1
print(max_dist)
print(count)






