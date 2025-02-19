import sys
from collections import deque
sys.stdin = open("input_2.txt", "r")

# 바이러스는 1초마다 상하좌우 방향으로 증식
# 바이러스는 번호가 낮은 순서대로 증식
# 증식할 때, 이미 바이러스가 있으면 증식 못함

# DFS로 구현, stack 자료구조 선입후출
n, m = map(int, input().split())
virus_loc = {}
for i in range(1, m+1):
    virus_loc[i] = deque()

grid = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# s는 특정 시간, (x, y)는 특정 위치
# s초에 (x, y) 좌표에 증식한 바이러스 종류를 구해야함
# 2초에 (3, 2)에 증식한 바이러스의 종류?
s, a, b = map(int, input().split())

for num in range(1, m+1):
    for i in range(n):
        for j in range(n):
            if grid[i][j]==num:
                virus_loc[num].append((i, j))

print(virus_loc)

# deque 라이브러리를 활용한 bfs 알고리즘 구현
# 처음엔 dfs로 구현하려다가 stack을 쓰면 못 만든다는 걸 알고 BFS/deque로 바꿈
def bfs(target_time, target_x, target_y):
    c_time = 0
    while c_time!=target_time:
        for i in range(1, m+1):
            # stack = virus_loc[i]
            # x, y = stack.pop()
            iter_len = len(virus_loc[i])
            for _ in range(iter_len):
                x, y = virus_loc[i].popleft()
                for d in range(4):
                    nx, ny = x+dx[d], y+dy[d]
                    if 0<=nx<n and 0<=ny<n and grid[nx][ny]==0:
                        grid[nx][ny]=i
                        virus_loc[i].append((nx, ny))
        c_time+=1
    print(grid)
    return grid[target_x-1][target_y-1]


print(bfs(s, a, b))

# print(grid)
# print(virus_loc)
# def dfs():