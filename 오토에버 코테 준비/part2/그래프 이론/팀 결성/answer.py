import sys

sys.stdin = open("input.txt", "r")

def find_parent(parent, x):
    if parent[x]!=x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a > b:
        parent[a]=b
    else:
        parent[b]=a

# 팀 수 0~n, 총 n+1개 팀
# 팀합치기 연산 수 m
n, m = map(int, sys.stdin.readline().rstrip().split())

parent = [0] * (n+1)

for i in range(0, n+1):
    parent[i] = i

for _ in range(m):
    # a는 0 or 1. 0은 팀을 합친다. 1은 같은 팀인지 확인
    cal, a, b = map(int, sys.stdin.readline().rstrip().split())
    if cal == 0:
        union_parent(parent,a, b)
    else:
        if find_parent(parent, a)==find_parent(parent,b):
            print('YES')
        else:
            print('NO')