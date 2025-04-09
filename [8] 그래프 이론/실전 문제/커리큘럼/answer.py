import sys
from collections import deque
import copy

sys.stdin = open("input.txt", "r")

# 첫째 줄 : 동빈이가 듣고자 하는 강의의 수 N
# 다음 N 개의 줄에는 각 강의의 강의 시간, 그 강의를 듣기 위해 먼저 들어야하는 강의들의 번호가 자연수로 주어짐
# 각 강의의 번호는 1부터 N까지 구성되며, 각 줄은 -1로 끝남

# 노드의 개수 입력받기
v = int(sys.stdin.readline().rstrip())
# 모든 노드에 대한 진입 차수는 0으로 초기화
indegree = [0] * (v+1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = [[] for i in range(v+1)]

# 각 강의 시간을 0으로 초기화
time = [0] * (v+1)

# 방향 그래프의 모든 간선 정보 입력 받기
for i in range(1, v+1):
    data = list(map(int, sys.stdin.readline().rstrip().split()))
    time[i] = data[0]
    for x in data[1:-1]:
        indegree[i] +=1
        graph[x].append(i)

# 위상 정렬 함수
def topology_sort():
    result = copy.deepcopy(time)
    q = deque()

    for i in range(1, v+1):
        if indegree[i]==0:
            q.append(i)

    while q:
        now = q.popleft()

        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i]-=1

            if indegree[i]==0:
                q.append(i)

    for i in range(1, v+1):
        print(result[i])

topology_sort()
