import heapq
import sys

# 첫째 줄에 도시의 개수 N, 통로의 개수 M, 메시지를 보내고자하는 도시 C가 주어짐
# 둘째 줄~(M+1) 줄에 걸쳐서 통로에 대한 정보 XYZ가 주어짐
# 특정 도시 X에서 다른 특정 도시 Y로 이어지는 통로가 있으며, 메시지가 전달되는 시간이 Z라는 의미임
# (1 <= X, Y <= N, 1 <= Z <= 1000)
sys.stdin = open("input.txt", "r")
INF = int(1e9)

# 노드의 개수, 간선의 개수, 시작 노드를 입력받기
n, m, start = map(int, sys.stdin.readline().rstrip().split())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph =[[] for i in range(n+1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

for _ in range(m):
    x, y, z = map(int, sys.stdin.readline().rstrip().split())
    # x번 노드에서 y번 노드로 가는 비용이 z라는 의미
    graph[x].append((y, z))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 거리 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보를 꺼내기
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘을 수행
dijkstra(start)

# 도달할 수 있는 노드의 개수
count = 0
# 도달할 수 있는 노드 중에서, 가장 멀리 있는 노드와 최단 거리
max_distance = 0
for d in distance:
    # 도달할 수 있는 노드인 경우
    if d!=INF:
        count+=1
        max_distance = max(max_distance, d)

# 시작 노드는 제외해야 하므로 count-1을 출력
print(count-1, max_distance)