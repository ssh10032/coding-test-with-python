# 팀 합치기는 두 팀을 합치는 연산이다
# '같은 팀 여부 확인' 연산은 특정한 두 학생이 같은 팀에 속하는지를 확인하는 연산이다.

# 팀 합치기 연산은 0 a b 형태로 주어짐 > a 학생 팀과 b 학생 팀을 합친다
# 같은 팀 여부 확인 연산은 1 a b 형태로 주어짐 > a 학생과 b 학생이 같은 팀인지 확인
import sys

sys.stdin = open("input.txt", "r")

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, sys.stdin.readline().rstrip().split())
parent =[0] * (n+1)

for i in range(0, n+1):
    parent[i] = i

for i in range(m):
    oper, a, b = map(int, sys.stdin.readline().rstrip().split())
    if oper == 0:
        union_parent(parent, a, b)
    elif oper == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")