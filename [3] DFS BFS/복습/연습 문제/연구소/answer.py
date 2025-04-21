import sys
import itertools
import copy

sys.stdin = open("input.txt", "r")

# 바이러스는 상하좌우로 퍼져나갈 수 있음
# 새로 세울 수 있는 벽은 3개, 꼭 3개를 세워야함
# 0 : 빈칸
# 1 : 벽
# 2 : 바이러스
# 바이러스가 퍼질 수 없는 곳을 안전 영역이라고 할때
# 안전 영역 크기의 최댓값을 구하는 프로그램 작성
n, m = map(int, sys.stdin.readline().rstrip().split())

graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 빈칸과 바이러스 위치 저장
# 빈칸 중에서 3개를 골라 벽으로 세워야함
empty_spaces = []
virus_positions = []

for i in range(n):
    for j in range(m):
        if graph[i][j]==0:
            empty_spaces.append((i, j))
        elif graph[i][j]==2:
            virus_positions.append((i, j))

def spread_virus(grid):
    stack = virus_positions[:]
    while stack:
        x, y = stack.pop()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0<=nx<n and 0<=ny<m and grid[nx][ny]==0:
                grid[nx][ny]=2
                stack.append((nx, ny))

def get_safe_area(grid):
    safe_count = sum(row.count(0) for row in grid)
    return safe_count