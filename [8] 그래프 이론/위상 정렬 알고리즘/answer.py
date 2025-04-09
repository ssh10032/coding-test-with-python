import sys
from collections import deque

sys.stdin = open("input.txt", "r")

# 노드, 간선의 개수 입력 받기
v, e = map(int, sys.stdin.readline().rstrip().split())

# 모든 노드에 대한 진입 차수는 0으로 초기화
indegree = [0] * (v+1)

# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
graph = [[] for i in range(v+1)]

# 방향 그래프의 모든 간선 정보를 입력받기
for _ in range(e):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b) # 정점 a에서 b로 이동 가능
    # 진입 차수를 1 중가
    indegree[b] += 1

# 위상 정렬 함수
def topology_sort():
    result = []
    q = deque()

    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입 차수에서 1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입 차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)
    for i in result:
        print(i, end=' ')


# 시간 복잡도는 O(V+E)
# 차례대로 모든 노드를 확인하면서 해당 노드에서 출발하는 간선을 차례대로 제거해야함
# 결과적으로 노드와 간선을 모두 확인한다는 측면에서 O(V+E)의 시간이 소요됨
topology_sort()