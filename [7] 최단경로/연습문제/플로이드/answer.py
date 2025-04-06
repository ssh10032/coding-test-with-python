import sys

sys.stdin = open("input.txt", "r")

# 도시의 개수
n = int(sys.stdin.readline().rstrip())
# 버스의 개수
m = int(sys.stdin.readline().rstrip())

INF = int(1e9)
graph = [[INF] * (n+1) for _ in range(n+1)]
for a in range(1, n+1):
    for b in range(1, n+1):
        if a==b:
            graph[a][b]=0

# print(graph)
# 버스의 정보
# 버스의 시작 도시 a, 도착 도시 b, 타는데 필요한 비용 c
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    # 내가 부족했던 점
    # 같은 노선의 버스가 있는 경우가 있을 수 있음
    # 그럴땐, 비용이 작은 버스의 비용으로 넣어야함!!!!
    # graph[a][b] = c >> 잘못짠부분
    graph[a][b] = min(graph[a][b], c)

# print(graph)

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

# print(graph)

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print("infinity", end=" ")
        else:
            print(graph[a][b], end=" ")
    print()