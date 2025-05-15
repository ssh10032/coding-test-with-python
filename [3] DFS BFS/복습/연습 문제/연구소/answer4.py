import sys

# 연구소 크기는 n * m
# 빈칸, 벽, 바이러스로 이루어짐
# 바이러스는 상하좌우로 퍼질수있음
# 새로 세울 수 있는 벽의 개수는 3
# 0은 빈칸, 1은 벽, 2는 바이러스
# sys.stdin = open("input.txt", "r")
sys.stdin = open("input2.txt", "r")

n, m = map(int, sys.stdin.readline().rstrip().split())

graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
temp = [[0]*m for _ in range(n)]
print(graph)
print(temp)
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
result = 0

def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx>=0 and nx<n and ny>=0 and ny<m:
            if temp[nx][ny]==0:
                temp[nx][ny]=2
                virus(nx, ny)

def get_score():
    score=0
    for i in range(n):
        for j in range(m):
            if temp[i][j]==0:
                score+=1
    return score

def dfs(count):
    global result
    if count == 3:
        # 바이러스 확산할때만 원본 graph를 건들지말고, 복사본 temp를 사용함
        for i in range(n):
            for j in range(m):
                temp[i][j]=graph[i][j]
        for i in range(n):
            for j in range(m):
                if temp[i][j]==2:
                    virus(i, j)
        result = max(get_score(), result)
        return

    for i in range(n):
        for j in range(m):
            if graph[i][j]==0:
                # 벽을 만든 경우 count+1, graph 수정후 재귀호출
                count+=1
                graph[i][j]=1
                dfs(count)
                # 재귀 호출후 다른 경우에서도 재귀호출이 이루어질수 있도록
                # count와 graph를 원래대로 되돌려놓음
                count-=1
                graph[i][j]=0
                # dfs(count)

# def dfs2(count):
#     global result
#     if count==3:
#         for i in range(n):
#             for j in range(m):
#                 temp[i][j] = graph[i][j]
#         for i in range(n):
#             for j in range(m):
#                 if temp[i][j]==2:
#                     virus(i, j)
#         result = max(result, get_score())
#         return
#     for i in range(n):
#         for j in range(m):
#             if graph[i][j]==0:
#                 graph[i][j]=1
#                 count+=1
#                 dfs(count)
#                 graph[i][j]=0
#                 count-=1

dfs(0)
print(result)


