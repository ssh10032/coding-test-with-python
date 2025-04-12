import sys
from collections import deque

sys.stdin = open("input.txt", "r")

# 순위를 알아내는 문제이므로
# 위상 정렬 문제가 맞았음!

# 떠올리기 어려웠던 아이디어들

#1 순위간 연결 관계를 2차원 그래프로 표현한 것
# 나는 1차원 리스트로 하려고 해서, 풀리지 않았던 것 같다..
# 상대 순위를 통해서 두 노드 간 우선 순위를 뒤집어야하므로,
# 1차원 리스트보다 2차원 행렬로 접근하는 것이 올바른 접근 방법이었다...

#2 큐의 길이를 체크해서, 사이클 여부를 점검하는 것
# deque를 통해 위상 정렬을 하는 방식은
# 차수가 가장 낮은 노드를 시작으로
# popleft()로 가장 낮은 차수 노드 추출
# graph를 활용해 해당 노드와 연결된 노드를 추출하고, 차수를 낮춤.
# 여기서 차수가 0이된 노드를 queue에 삽입.

# 그래서 정상적인 순위가 유지되면 길이가 1로 유지될 것이다..

# 반복문이 실행하는 동안
# 길이가 2인 경우에는 순위가 모호한 노드 두개가 존재한다는 뜻 >> 정보가 잘못됨. 오류가 있음 >> ???
# 길이가 0인 경우에는 순위를 알 수 없는 노드가 존재한다는 뜻 >> IMPOSSIBLE
for tc in range(int(sys.stdin.readline().rstrip())):
    # 팀 수
    n = int(sys.stdin.readline().rstrip())

    # 모든 노드에 대한 진입 차수는 0으로 초기화
    indegree = [0] * (n+1)

    ##### 간선 정보를 담기 위한 2차원 인접 행렬 초기화 #####
    graph = [[False] * (n+1) for i in range(n+1)]
    #################################################

    # 작년 순위 정보
    data = list(map(int, sys.stdin.readline().rstrip().split()))

    # 작년 순위 정보를 토대로 인접 행렬 초기화
    for i in range(n):
        for j in range(i+1, n):
            graph[data[i]][data[j]]=True
            indegree[data[j]] += 1

    # 올해 상대적 순위 정보 입력
    m = int(sys.stdin.readline().rstrip())
    for i in range(m):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        # 간선 방향 뒤집기
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

    # 위상 정렬 시작
    result = []

    # 큐 기능을 위한 deque 라이브러리 사용
    q = deque()

    for i in range(1, n+1):
        if indegree[i]==0:
            q.append(i)

    # certain 변수 : 순위가 확실한지 여부
    # cycle 변수 : 싸이클이 발생하는지 여부
    certain = True
    cycle = False

    # 노드(팀)의 개수만큼 반복
    for i in range(n):
        # 모든 반복문이 돌기전에
        # 큐가 비었다 == 싸이클이 발생해서 >> 순위를 알 수 없는 노드가 있다.
        if len(q)==0:
            cycle = True
            break
        # 모든 반복문이 돌기전에
        # 큐의 길이가 1보다 크다 == 순위 관계가 명확하지 않은 두개 이상의 노드들이 있다.
        # 순위 관계가 명확하면 큐에는 하나의 노드만 들어올 것이기 때문.
        if len(q)>=2:
            certain = False
            break
        now = q.popleft()
        result.append(now)

        for j in range(1, n+1):
            if graph[now][j]:
                indegree[j]-=1
                if indegree[j]==0:
                    q.append(j)

    # 싸이클이 발생하기 때문에, 순위를 전혀 알 수 없는 노드가 있다
    if cycle:
        print("IMPOSSIBLE")
    # 서로 순위를 비교할 수 없는 노드들이 있다.
    elif not certain:
        print("?")
    else:
        for i in result:
            print(i, end=" ")
        print()