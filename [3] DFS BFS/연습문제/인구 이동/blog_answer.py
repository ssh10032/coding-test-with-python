import sys
from collections import deque

# BFS deque는 선입선출
# input 1 : 1
# input 2 : 0
# input 3 : 1
# input 4 : 2
# input 5 : 3
sys.stdin = open("input.txt", "r")
# sys.stdin = open("input_2.txt", "r")
# sys.stdin = open("input_3.txt", "r")
# sys.stdin = open("input_4.txt", "r")
# sys.stdin = open("input_5.txt", "r")

N, L, R = map(int, input().split())

c_list = [list(map(int, input().split())) for _ in range(N)]

# print(c_list)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

queue = deque()
def bfs(x, y):
    union = []
    queue.append((x, y))
    union.append((x, y))
    while queue:
        x, y = queue.popleft()
        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]
            if 0<=nx<N and 0<=ny<N and visited[nx][ny]==0:
                if L<=abs(c_list[x][y]-c_list[nx][ny])<=R:
                    queue.append((nx, ny))
                    union.append((nx, ny))
                    visited[nx][ny]=1

    if len(union)<=1:
        return 0
    union_spy = sum(c_list[i][j] for i, j in union)//len(union)
    for i, j in union:
        c_list[i][j] = union_spy
    return 1

# 하나의 좌표에 대해서 bfs 탐색을 할 수 있도록 함수로 구현
# 모든 도시 인덱스에 대해서 bfs 함수를 호출
# 방문 여부를 체크하는 행렬을 만들어서, 체크 안해도 되면 패스
# bfs 함수에서 반환된 값을 통해서 무한 루프를 탈출할지 결정
#
day = 0
while True:
    stop = 0
    # 이렇게 초기화해버리면 같은 객체를 참조
    # visited = [[0] * N] * N
    # (0, 1)값을 바꾸면 1열 값이 전부 바뀌어버림
    # 주의할 것
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j]==0:
                visited[i][j] = 1
                stop += bfs(i, j)
    if stop == 0:
        break
    day+=1
print(day)

