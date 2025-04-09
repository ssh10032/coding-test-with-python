import sys

sys.stdin = open("input.txt", "r")

# 마을은 N개의 집과 M개의 길로 이루어져 있음
# 마을을 2개의 분리된 마을로 분할

# 마을을 분할할 때에는,
# 마을 안에 집들이 서로 연결되어 있도록 분할해야함
# >> 분리된 마을 안에 있는 임의의 두 집 사이에는 항상 경로가 존재해야함

# 두 마을 사이의 길들은 없앨 수 있음
# 각 분리된 마을 안에서도 두 집 사이에 경로가 존재하게 하면서, 길을 더 없앨 수 있음

# 위 조건을 만족하도록 길을 없애고, 나머지 길의 유지비의 합을 최소로 만들어야함.


# 구현 아이디어
#1 크루스칼 알고리즘으로 최소 신장 트리를 찾는다.
#2 최소 신장 트리를 구성하는 간선 중 가장 비용이 큰 간선을 제거하면 됨!

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(union 연산?)의 개수 입력
v, e = map(int, sys.stdin.readline().rstrip().split())
parent = [0] * (v+1)

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블 상에서, 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

# 모든 간선에 대한 정보를 입력 받기
for _ in range(e):
    a, b, cost = map(int, sys.stdin.readline().rstrip().split())
    edges.append((cost, a, b))

# 간선을 비용 순으로 정렬
edges.sort()
last = 0

# 간선을 하나씩 확인
for edge in edges:
    cost, a, b = edge
    # 싸이클이 발생하지 않는 경우에만 집합 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        last = cost

print(result - last)