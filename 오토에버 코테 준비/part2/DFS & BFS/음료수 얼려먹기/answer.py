import sys

# sys.stdin = open("input.txt", "r")
sys.stdin = open("input2.txt", "r")

n, m = map(int, sys.stdin.readline().rstrip().split())

ddd = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]

print(ddd)
# dfs stack 선입후출, 재귀 호출
def dfs(x, y):
    if x <= -1 or x>=n or y<=-1 or y>=m:
        return False
    if ddd[x][y]==0:
        ddd[x][y]=1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

result = 0

for i in range(n):
    for j in range(m):
        if dfs(i, j)==True:
            result+=1

print(result)