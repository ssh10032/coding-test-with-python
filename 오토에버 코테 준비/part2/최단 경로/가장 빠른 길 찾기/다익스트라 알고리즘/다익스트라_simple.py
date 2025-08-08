import sys

sys.stdin = open("input.txt", "r")
INF = int(1e9)

n, m = map(int, sys.stdin.readline().rstrip().split())

start = int(sys.stdin.readline().rstrip())

# 연결 정보 담는 리스트
graph = [[] for i in range(n+1)]
# 방문 여부 체크 리스트
visited = [False] * (n+1)
# 최단 거리 테이블 모두 무한으로 초기화
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append((b, c))

def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if distance[i]<min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True

        for j in graph[now]:
            cost = distance[now]+j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
dijkstra(start)

for i in range(1, n+1):
    if distance[i]==INF:
        print("infinity")
    else:
        print(distance[i])
