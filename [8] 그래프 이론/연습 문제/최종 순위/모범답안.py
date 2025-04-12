import sys
from collections import deque

sys.stdin = open("input.txt", "r")

for tc in range(int(sys.stdin.readline().rstrip())):
    # 노드의 개수 입력 받기
    n = int(sys.stdin.readline().rstrip())
    print(n)
    # 모든 노드에 대한 진입 차수는 0으로 초기화
    indegree = [0] * (n+1)
    # 간선 정보를 담기 위한 인접 행렬 초기화
    # 2차원 행렬로 만듬?
    graph = [[False] * (n+1) for i in range(n+1)]
    print(graph)
    # 작년 순위 정보 입력
    data = list(map(int, sys.stdin.readline().rstrip().split()))
    print(data)
    # 방향 그래프의 간선 정보 초기화
    for i in range(n):
        for j in range(i+1, n):
            graph[data[i]][data[j]]=True
            indegree[data[j]] += 1

    # 올해 변경된 순위 정보 입력
    m = int(sys.stdin.readline().rstrip())
    for i in range(m):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        # 간선의 방향 뒤집기
        if graph[a][b]:
            graph[a][b]=False
            graph[b][a]=True
            indegree[a]+=1
            indegree[b]-=1
        else:
            graph[a][b]=True
            graph[b][a]=False
            indegree[a]-=1
            indegree[b]+=1
    print(graph)
    # 위상 정렬 시작
    result = []
    # 큐 기능을 위한 deque 라이브러리 사용
    q = deque()

    # 처음 시작할 때는 진입 차수가 0인 노드를 큐에 삽입
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    certain = True
    cycle = False

    # 노드의 개수만큼 반복
    for i in range(n):
        # 큐가 비어있으면 사이클 발생했다는 의미
        if len(q)==0:
            cycle = True
            break
        # 큐의 원소가 2개 이상이라면,
        # 가능한 정렬 결과가 여러개라는 의미
        if len(q)>=2:
            certain = False
            break
        now = q.popleft()
        result.append(now)

        for j in range(1, n+1):
            if graph[now][j]:
                indegree[j]-=1
            # 새롭게 진입 차수가 0이 되는 노드를 큐에 삽입
            if indegree[j] == 0:
                q.append(j)

    if cycle:
        print("IMPOSSIBLE")
    elif not certain:
        print("?")
    else:
        for i in result:
            print(i, end=' ')
        print()