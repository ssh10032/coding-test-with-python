import sys
from collections import deque

sys.stdin = open("input.txt", "r")

n, l, r = map(int, sys.stdin.readline().rstrip().split())

graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

result = 0

def process(x, y, index):
    # (x, y) 위치에 연결된 나라 정보를 담는 리스트
    united = []
    united.append((x, y))
    # BFS를 위한 큐 자료구조
    q = deque()
    q.append((x, y))
    union[x][y] = index
    summary = graph[x][y]
    # 연합된 국가의 수
    count = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<n and union[nx][ny]==-1:
                if l<=abs(graph[nx][ny]-graph[x][y])<=r:
                    q.append((nx, ny))
                    # 연합에 추가
                    union[nx][ny]=index
                    summary += graph[nx][ny]
                    count+=1
                    united.append((nx, ny))
    for i, j in united:
        graph[i][j] = summary//count
    return count

total_count=0

while True:
    union = [[-1] * n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j]==-1:
                process(i, j, index)
                index+=1
    if index == n * n:
        break
    total_count+=1

print(total_count)
