import sys

sys.stdin = open("input.txt", "r")

# 0 빈칸, 1은 벽, 2는 바이러스
# 바이러스는 상하좌우로 퍼짐
# 벽은 3개 세울 수 있음
# 안전 지대 최대 영역 수를 출력
n, m = map(int, sys.stdin.readline().rstrip().split())

graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
temp = [[0] * m for _ in range(n)]

print(graph)

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

result = 0

# 깊이 우선 탐색으로 각 바이러스 사방으로 퍼지게 구현
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 상하좌우로 바이러스 퍼질 수 있는 경우
        if nx >= 0 and nx < n and ny>=0 and ny <m:
            if temp[nx][ny]==0:
                temp[nx][ny]=2
                virus(nx, ny)

def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j]==0:
                score+=1
    return score

def dfs(count):
    global result
    # 울타리가 3개 설치된 경우
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = graph[i][j]
        for i in range(n):
            for j in range(m):
                if temp[i][j]==2:
                    virus(i, j)
        result = max(result, get_score())
        return
    # 빈 공간에 울타리 설치
    for i in range(n):
        for j in range(m):
            if graph[i][j]==0:
                graph[i][j] = 1
                count += 1
                dfs(count)
                graph[i][j] = 0
                count-=1

dfs(0)
print(result)
