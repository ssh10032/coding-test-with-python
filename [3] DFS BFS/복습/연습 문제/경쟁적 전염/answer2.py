import sys
from collections import deque

# n * n 시험관
# 바이러스 종류 : 1~K까지
# 1초마다 상하좌우로 증식
# 매초 번호가 낮은 종류의 바이러스 먼저 증식
# 증식 과정에서 이미 다른 바이러스가 있으면, 다른 바이러스 증식 못함

# s초가 지난 후에 (x, y)에 존재하는 바이러스 종류를 출력하는 프로그램 작성

# 접근 방식
# 큐 자료구조와 bfs 알고리즘을 사용

# sys.stdin = open("input.txt", "r")
sys.stdin = open("input2.txt", "r")

n, k = map(int, sys.stdin.readline().rstrip().split())

graph = []
data = []

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))
    for j in range(n):
        if graph[i][j]!=0:
            # 우선 순위 큐로 만들기 위해서
            # 바이러스 종류, 시간, xy 좌표 순으로 리스트 할당
            data.append((graph[i][j], 0, i, j))

data.sort()
q = deque(data)

target_s, target_x, target_y = map(int, sys.stdin.readline().rstrip().split())

dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]


while q:
    print(q)
    virus, s, x, y = q.popleft()
    # print("virus type:", virus)
    # print("time : ", s)
    # print("x : ", x)
    # print("y : ", y)
    if s == target_s:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n:
            if graph[nx][ny]==0:
                graph[nx][ny]=virus
                q.append((virus, s+1, nx, ny))


print(graph[target_x-1][target_y-1])
