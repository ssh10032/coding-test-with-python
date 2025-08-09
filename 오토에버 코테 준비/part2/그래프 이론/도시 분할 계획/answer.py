import sys

sys.stdin = open("input.txt", "r")
# 마을은 n개의 집과 m개의 길로 이루어짐
v, e = map(int, sys.stdin.readline().rstrip().split())

parent = [0] * (v+1)

for i in range(1, v+1):
    parent[i] = i

edges = []
result = 0

def find_parent(parent, x):
    if parent[x]!=x:
        parent[x]=find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b]=a
    else:
        parent[a]=b

for _ in range(e):
    a, b, cost = map(int, sys.stdin.readline().rstrip().split())
    edges.append((cost, a, b))

edges.sort()
last = 0

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result+=cost
        last = cost

print(result-last)