import sys

sys.stdin = open("input_f.txt", "r")

INF = int(1e9)

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
# 2차원 리스트로 연결 관계 표현. 무한으로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a==b:
            graph[a][b]=0

for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().rstrip().split())
    graph[a][b] = c

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b]==INF:
            print("infinity")
        else:
            print(graph[a][b], end=' ')
    print()