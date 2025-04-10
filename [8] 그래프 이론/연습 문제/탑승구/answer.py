import sys
from collections import deque

sys.stdin = open("input.txt", "r")

# 공항에는 G개의 탑승구가 있음. 각각 탑승구는 1번부터 G번까지의 번호로 구분됨
# P개의 비행기가 차례대로 도착할 예정
# i 번째 비행기를 1번부터 g번째 탑승구 중 하나에 영구적으로 도킹해야함.
# 다른 비행기가 도킹하지 않은 탑승구에만 도킹 가능.

# P개의 비행기를 순서대로 도킹하다가, 어떤 탑승구에도 도킹할 수 없는 비행기가 나오면,
# 그 시점에서 공항의 운행을 중지함.

# 공항의 관리자는 최대한 많은 비행기를 공항에 도킹하고자 함.
# 비행기를 최대 몇 대 도킹할 수 있는 지 출력

# 첫째 줄에는 탑승구의 수 G가 주어짐
# 둘째 줄에는 비행기의 수 P가 주어짐
# 다음 P개의 줄에는 각 비행기가 도킹할 수 있는 탑승구의 정보가 주어짐
# g(1<=g<=G)
# i번째 비행기가 1번부터 g번째 탑승구 중 하나에 도킹할 수 있다는 의미임.



# 내 접근 방식
# 각 탑승구의 차수를 기록하고
# 위상 정렬 알고리즘으로 풀어볼려고 했었음

# 차수가 낮은 탑승구부터 줄여서
# 마지막에 차수가 0인 탑승구를 출력?
# >> 잘못된 접근, 애초에 비행기 하나 할당해도 차수가 줄어도 0이 안되는 경우도 있음

# answer2 에서 다시 생각해보자
g = int(sys.stdin.readline().rstrip())
p = int(sys.stdin.readline().rstrip())

indegree = [0] * (g+1)

print(g)
print(p)

graph = [[] for i in range(p+1)]
for i in range(1, p+1):
    dok = int(sys.stdin.readline().rstrip())
    graph[i].append(dok)
    for j in range(1, dok+1):
        indegree[j]+=1
print(graph)

def topology_sort():
    result = []
    q = deque()

    for i in range(1, g+1):
        if indegree[i] == 1:
            q.append(i)
    while q:
        now = q.popleft()
        result.append(now)
