import sys
from collections import deque

sys.stdin = open("input.txt", "r")

n, l, r = map(int, sys.stdin.readline().rstrip().split())

graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

print(graph)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

result = 0

def process(x, y, index):
    united = []
    united.append((x, y))

    q = deque()
    q.append((x, y))
    union[x][y] = index
    # 연합된 나라들의 총 인구수를 저장할 변수
    summary = graph[x][y]
    # 연합된 국가의 수
    count = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 인접한 국가가 아직 어떤 연합에 속하지 않았을 경우
            if 0<=nx<n and 0<=ny<n and union[nx][ny]==-1:
                # 연합 조건인 인구수 차이가 만족할 경우
                if l<=abs(graph[nx][ny]-graph[x][y])<=r:
                    # 해당 국가 큐에 추가
                    q.append((nx, ny))
                    # 연합 정보 리스트 갱신
                    union[nx][ny]=index
                    # 연합 총 인구수 갱신
                    summary+=graph[nx][ny]
                    count+=1
                    united.append((nx, ny))
    for i, j in united:
        graph[i][j] = summary//count
    return count

total_count = 0

while True:
    # 연합 정보 리스트
    union = [[-1] * n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j]==-1:
                process(i, j, index)
                index+=1
    # 나라 간 연합이 존재하지 않을 경우
    if index == n*n:
        break
    # 인구 이동수
    # 연합이 이루어지고, 연합끼리 인구 이동이 일어날 때 >> 인구이동이 한번 일어난 것으로 침
    total_count+=1

print(total_count)