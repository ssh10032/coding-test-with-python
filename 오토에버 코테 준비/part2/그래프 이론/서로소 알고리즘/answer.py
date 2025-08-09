import sys

sys.stdin = open("input.txt", "r")

def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

def find_parent2(parent, x):
    if parent[x]!=x:
        parent[x]=find_parent2(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent2(parent, a)
    b = find_parent2(parent, b)

    if a<b:
        parent[b]=a
    else:
        parent[a]=b

# 노드 개수 vertex, 간선 개수 edge
v, e = map(int, sys.stdin.readline().rstrip().split())
parent = [0] * (v+1)

for i in range(1, v+1):
    parent[i] = i

for i in range(e):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    union_parent(parent, a, b)

print('각 원소가 속하는 집합 : ', end=' ')
for i in range(1, v+1):
    print(find_parent2(parent, i), end = ' ')

print()

print('부모 테이블: ', end = ' ')
for i in range(1, v+1):
    print(parent[i], end = ' ')

