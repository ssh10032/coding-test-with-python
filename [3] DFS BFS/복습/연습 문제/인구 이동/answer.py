import sys
from collections import deque

sys.stdin = open("input_5.txt", "r")

# l명 이상, r명 이하라면, 두 나라가 공유하는 국경선이 열림
n, l, r = map(int, sys.stdin.readline().rstrip().split())

sply = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

print(sply)

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

result = 0

def process(x, y, index):
    united = []
    united.append((x, y))
    q = deque()
    q.append((x, y))
    union[x][y] = index
    summary = sply[x][y]
    count = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 인접한 나라를 확인, 연합 소속이 안되어 있는 경우
            if 0<=nx<n and 0<=ny<n and union[nx][ny]==-1:
                # 인접 나라와 인구 차이 확인
                # l명 이상 r명 이하인 경우
                if l<=abs(sply[nx][ny]-sply[x][y])<=r:
                    q.append((nx, ny))
                    union[nx][ny]=index
                    summary +=sply[nx][ny]
                    count+=1
                    united.append((nx,ny))
    # 연합 국가까리 인구 분배
    for i, j in united:
        sply[i][j]=summary//count
    return count

total_count = 0

# 인구 이동이 없을 때까지 반복
while True:
    union = [[-1] * n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j]==-1:
                process(i, j, index)
                index+=1
    # 인구 이동이 끝난 경우
    if index == n*n:
        print(index)
        break
    total_count+=1

print(total_count)