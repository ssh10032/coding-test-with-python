import sys

# N개의 집, M개의 도로
# 각 집은 0~N-1번 번호로 구별
# 모든 도로에는 가로등이 구비, 가로등을 하루동안 켜는 비용은 도로의 길이와 동일
# 정부에서 일부 가로등을 비활성홯되,
# 마을에 있는 임의의 두 집에 대하여 가로등이 켜진 도로만으로도 오갈 수 있도록 만들고자함
# 결과적으로 일부 가로등만 비활성화하여 최대한 많은 금액을 절약하고자 함.

# 내 접근 방식
# 모든 마을의 집이 오갈 수 있게 만들어야됨. 비용은 최소로.
# 최소 신장 트리 문제라고 생각함
# 크루스칼 알고리즘으로 접근 가능
# 간선을 비용 순으로 정렬하는게 제일 중요!!
# 그 다음은, 비용 순으로 도로 간 두 집의
# 부모 노드를 찾고, union 연산을 함
# 그리고 result에 더하면, 최소 비용을 구할 수 있음!

# 일부 가로등을 비활성화하여 절약할 수 있는 최대 금액 출력
sys.stdin = open("input.txt", "r")

def find_parent(parent, x):
    if parent[x]!=x:
        parent[x]=find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, sys.stdin.readline().rstrip().split())

parent = [0] * n

edges = []
result = 0
total_cost = 0

for i in range(n):
    print(i, end= ' ')
    parent[i] = i
print()
for _ in range(m):
    # 집a와 집b 사이의 도로 비용 cost
    a, b, cost = map(int, sys.stdin.readline().rstrip().split())
    edges.append((cost, a, b))
    total_cost+=cost
# 도로 비용을 비용이 낮은 순으로 정렬
edges.sort()
print(edges)

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result+=cost

print(total_cost-result)