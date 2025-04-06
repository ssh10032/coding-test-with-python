import sys

# 문제 접근 : 학생 수가 500명, 도달 가능한지 체크
# 정확한 순위는 알필요 없고, 모든 학생의 성적과 비교할 수 있는지만 알면 된다~~
# O(N**3)의 플로이드 워셜 알고리즘으로 접근 가능

# 출발점이 정해져 있는 다익스트라 알고리즘보다는
# 모든 노드들을 비교해서 2차원 리스트에 기록하는
# 플로이드 워셜 알고리즘이 직관적으로 바로 구현할 수 있다는 생각이 들었음

sys.stdin = open("input.txt", "r")

# 성적 비교를 할 수 없는 경우에는 INF
INF = int(1e9)
n, m = map(int, sys.stdin.readline().rstrip().split())

graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b]=0

for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a][b]=1

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        print(graph[a][b], end=" ")
    print("")

result = 0
for a in range(1, n+1):
    count = 0
    for b in range(1, n+1):
        # if문의 조건을 and가 아닌 or로 해야함
        # 위에 반복문으로 순차적으로 기록되기 때문에 순위정보가 기록안되어있을 수 있기 때문
        if graph[a][b]!=INF or graph[b][a]!=INF:
            count+=1
    if count==n:
        result+=1
print(result)
