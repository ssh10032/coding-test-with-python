import sys

sys.stdin = open("input.txt", "r")

# 경로 압축 기법이 적용된
# find_parent 함수
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

# 노드의 개수와 간선(union 연산)의 개수 입력 받기
v, e = map(int, sys.stdin.readline().rstrip().split())
parent = [0] * (v+1)

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

# union 연산을 수행
for i in range(e):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    union_parent(parent, a, b)

print("각 원소가 속한 집합: ", end='')
for i in range(1, v+1):
    print(find_parent(parent, i), end=' ')

print()

# 부모 테이블 내용 출력
print("부모 테이블: ", end='')
for i in range(1, v+1):
    print(parent[i], end=' ')
