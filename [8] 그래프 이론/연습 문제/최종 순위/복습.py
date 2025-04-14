import sys
from collections import deque

sys.stdin = open("input.txt", "r")

for tc in range(int(sys.stdin.readline().rstrip())):
    # 노드의 개수 입력 받기
    n = int(sys.stdin.readline().rstrip())
    # 모든 노드에 대한 진입 차수는 0으로 초기화
    indegree = [0] * (n+1)
    # 간선 정보를 담기 위한 인접 행렬 초기화
    graph = [[False] * (n+1) for i in range(n+1)]

    # 작년 순위 정보 입력
    data = list(map(int, sys.stdin.readline().rstrip().split()))

    # 방향 그래프의 간선 정보 초기화
    for i in range(n):
        for j in range(i+1, n):
            graph[data[i]][data[j]]=True
            indegree[data[j]] +=1

    m = int(sys.stdin.readline().rstrip())
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        if graph[a][b]:
            graph[b][a]=True
            graph[a][b]=False
            indegree[a]+=1
            indegree[b]-=1
        else:
            graph[a][b]=True
            graph[b][a]=False
            indegree[b]+=1
            indegree[a]-=1

    # 위상 정렬 알고리즘 구현
    q = deque()
    for i in range(1, n+1):
        if indegree[i]==0:
            q.append(i)

    result = []
    cycle = False
    certain = True
    for i in range(n):
        if len(q)==0:
            cycle=True
            break
        if len(q)>=2:
            certain=False
            break
        now = q.popleft()
        result.append(now)

        for j in range(1, n+1):
            if graph[now][j]:
                indegree[j]-=1
                if indegree[j]==0:
                    q.append(j)
    if cycle:
        print("IMPOSSIBLE")
    elif not certain:
        print("???")
    else:
        for i in result:
            print(i, end=" ")
        print()