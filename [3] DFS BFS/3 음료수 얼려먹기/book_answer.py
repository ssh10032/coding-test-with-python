import sys

# DFS로 구현, 재귀 호출 사용

# input_1 정답 : 3
# input_2 정답 : 8
sys.stdin = open("input_2.txt", "r")

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    if graph[x][y]==0:
        graph[x][y]=1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j)==True:
            result+=1


print(result)