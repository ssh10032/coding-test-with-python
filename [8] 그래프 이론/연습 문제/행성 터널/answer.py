import sys

# 왕국은 N개의 행성으로 이루어져 있음
# 행성들을 효율적으로 지배하기 위해, 행성 연결 터널을 만들려고 함

# 행성은 3차원 좌표 위의 한 점으로 생각하면 됨
# 두 행성 A(x, y, z) B(a, b, c)를
# 터널로 연결하는 비용은 min(|x-a|,|y-b|,|z-c|) 임

# 터널을 총 N-1개 건설해서
# 모든 행성을 터널로 연결하는 최소 비용을 구해라

# 내 접근방식
# 모든 터널이 연결되어 있어야하고, 최소 비용을 구하는 문제이므로
# 최소 신장 트리 문제임
# 크루스칼 알고리즘으로 풀 수 있음!

# 행성간 좌표 입력받고
# 각 행성간 좌표로 간선 정보를 만들면 됨
sys.stdin = open("input.txt", "r")

n = int(sys.stdin.readline().rstrip())

parent = [0] * n

for i in range(n):
    parent[i]=i

def find_parent(parent, x):
    if parent[x]!=x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

planets = []
edges = []
for _ in range(n):
    x, y, z = map(int, sys.stdin.readline().rstrip().split())
    planets.append((x, y, z))

for i in range(n):
    p1 = planets[i]
    for j in range(i+1, n):
        p2 = planets[j]
        cost = min(abs(p1[0]-p2[0]), abs(p1[1]-p2[1]), abs(p1[2]-p2[2]))
        edges.append((cost, i, j))

edges.sort()
print(edges)
result = 0

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a)!=find_parent(parent, b):
        union_parent(parent, a, b)
        result+=cost

print(result)