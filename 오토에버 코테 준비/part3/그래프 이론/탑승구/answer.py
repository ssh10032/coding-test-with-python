import sys

sys.stdin = open("input.txt", "r")

def find_parent(parent, x):
    if parent[x]!=x:
        parent[x]=find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a>b:
        parent[a]=b
    else:
        parent[b]=a

g = int(sys.stdin.readline().rstrip())
p = int(sys.stdin.readline().rstrip())
parent = [0] * (g+1)

for i in range(1, g+1):
    parent[i] = i

result = 0

for _ in range(p):
    data = find_parent(parent, int(sys.stdin.readline().rstrip()))
    if data == 0:
        break
    union_parent(parent, data, data-1)
    result+=1
print(result)