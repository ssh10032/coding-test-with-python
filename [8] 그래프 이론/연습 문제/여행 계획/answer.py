import sys

sys.stdin = open("input.txt", "r")

# N개의 여행지 (1~N번 번호로 구분됨)
# 임의의 두 여행지 사이에는 두 여행지를 연결하는 도로가 존재
# 첫 줄 여행지 수 N과 여행 계획에 속한 여행지 수 M이 주어짐
# 다음 N개의 줄에 걸쳐 임의의 두 여행지가 서로 연결되어 있는지의 여부를 나타내는 N x N 행렬
# 마지막 줄에는 한울이의 여행 계획에 포함된 여행지들의 번호가 주어짐. 공백으로 구분.


# 내 접근법
# 연결 관계 n*n 행렬을 통해 부모 노드를 기록하는 것 까지는 했음

# 놓친 부분
# 연결 관계 행렬의 간선 정보를 통해서 union 연산을 시켜줬어야 했음!!
# 그래야 각 도시 별로 부모 노드가 같은지 확인하고, 여행 계획이 수행 가능한지
# 판단이 가능함!!
# answer2에서 다시 접근해보기
n, m = map(int, sys.stdin.readline().rstrip().split())

parent = [0] * (n+1)

for i in range(0, n+1):
    parent[i] = i

graph = []

for i in range(1, n+1):
    graph = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(0, len(graph)):
        if graph[j] == 1 and parent[j+1]>i:
            parent[j+1]=i

plan = list(map(int, sys.stdin.readline().rstrip().split()))


# print(graph)
#
# print(plan)
print(parent)
