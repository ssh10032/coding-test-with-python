import sys

# answer1 은 접근법이 틀린 것 같음
# answer2.py에서 다시 풀어보기
sys.stdin = open("input.txt", "r")

INF = int(1e9)
n, m = map(int, sys.stdin.readline().rstrip().split())
graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b]=0

for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    # b는 a보다 높은 성적
    graph[a][b]=-1
    # a는 b보다 낮은 성적
    graph[b][a]=1

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            if graph[a][k]==1 and graph[k][b]==-1:
                graph[a][b]=-1
                graph[b][a]=1

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b]=0

for a in range(1, n+1):
    for b in range(1, n+1):
        print(graph[a][b], end=" ")
    print(" ")

