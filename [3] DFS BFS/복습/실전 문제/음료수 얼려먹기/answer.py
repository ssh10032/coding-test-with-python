import sys

sys.stdin = open("input.txt", "r")
# 구멍 : 0, 칸막이 : 1
# 구멍 뚫린 부분 붙어있는 경우, 서로 연결된 것으로 간주
n, m = map(int, sys.stdin.readline().rstrip().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

def dfs(i, j, graph, visited):
    if 0<=i<n and 0<=j<m:
        if graph[i][j]==0 and visited[i][j]==0:
            visited[i][j]=1
            dfs(i+1, j, graph, visited)
            dfs(i-1, j, graph, visited)
            dfs(i, j+1, graph, visited)
            dfs(i, j-1, graph, visited)
            return True
        else:
            return False
    else:
        return False

print(graph)

visited = [[0] * m for _ in range(n)]
count = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j, graph, visited):
            count+=1

print(count)