import sys

sys.stdin = open("input.txt", "r")

g = int(sys.stdin.readline().rstrip())
p = int(sys.stdin.readline().rstrip())
plane = [int(sys.stdin.readline().rstrip()) for _ in range(p)]

# 그룹 초기화
parent = [0] * (g+1)
for i in range(1, g+1):
    parent[i] = i

def find_parent(parent, x):
    if parent[x]!=x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

count = 0
for p in plane:
    root = find_parent(parent, p)

    if root==0:
        break

    union_parent(parent, root, root-1)
    count+=1

print(count)