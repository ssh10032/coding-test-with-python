import sys

# 간선의 개수가 E개일 때
# O(ElogE)의 시간 복잡도를 가진다
# 크루스칼 알고리즘에서 시간이 가장 오래걸리는 작업은
# 간선을 정렬하는 작업임
# E개의 데이터를 정렬했을때의 시간 복잡도는 O(ElogE)이기 떄문이다.

sys.stdin = open("input.txt", "r")

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, sys.stdin.readline().rstrip().split())

parent = [0] * (v+1)

edges = []
result = 0

for i in range(1, v+1):
    parent[i] = i

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)

