import sys

sys.stdin = open("input.txt", "r")

n, m = map(int, sys.stdin.readline().rstrip().split())

parent = [0] * (n+1)

for i in range(0, n+1):
    parent[i] = i

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

for i in range(1, n+1):
    graph = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(len(graph)):
        if graph[j] == 1:
            union_parent(parent, i, j+1)

plan = list(map(int, sys.stdin.readline().rstrip().split()))

print(parent)
print(plan)

# 확인 여부 체크해주는 함수를 구현하는게 더 깔끔함!!!
# result = 0
# p = parent[plan[0]]
# for i in plan:
#     if p != parent[i]:
#         print("NO")
#         break
#     else:
#         continue
# print("YES")

def check(start):
    for p in plan:
        if parent[start]!=find_parent(parent, p):
            return "NO"
    return "YES"

print(check(plan[0]))