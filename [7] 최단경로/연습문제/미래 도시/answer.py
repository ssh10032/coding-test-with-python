import sys

sys.stdin = open("input.txt", "r")

# 첫째 줄에 회사의 개수 N과 경로의 개수 M이 공백으로 구분되어 차례대로 주어진다
# 둘째 줄부터 M+1번째 쭐에는 연결된 두 회사의 번호가 공백으로 구분되어 주어진다
# M+2번째 줄에는 X와 K가 공백으로 구분되어 주어진다

# 전형적인 플로드 워셜 알고리즘 문제
n, m = map(int, sys.stdin.readline().rstrip().split())
INF = int(1e9)
graph = [[INF] * (m+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b]=0
# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 거쳐 갈 노드 X와 최종 목적지 노드 K를 입력받기
x, k = map(int, input().split())

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

# 수행된 결과를 출력
distance = graph[1][k] + graph[k][x]

# 도달할 수 없는 경우, -1을 출력
if distance >= INF:
    print("-1")
else:
    print(distance)