import sys
from collections import deque

# bfs >> deque 선입선출
sys.stdin = open("input.txt", "r")

# 각 나라의 인구수 차이가 L명 이상, R명 이하
# >> 두 나라가 공유하는 국경선이 열림

# 국경선이 열리면
# 인구 이동 시작

# 국경선이 열려있어, 인접한 칸만을 이용해 이동할 수 있으면,
# 그 나라를 하루동안 연합이라고 부름

# 연합을 이루고 있는 각 칸의 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수)가 됨(소수점은 버림)
# 연합을 해체하고 모든 국경선을 닫음

# 인구 이동이 없을 때 까지 계속됨

N, L, R = map(int, input().split())

spy = [list(map(int, input().split())) for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
city_queue = deque((0, 0))
checked = [[0] * N] * N

print(spy)
while city_queue :
        x, y = city_queue.popleft()
        for dir_idx in range(4):
            nx = x + dx[dir_idx]
            ny = y + dy[dir_idx]
            if 0<=nx<N and 0<=ny<N:
                if L<=abs(spy[x][y]-spy[nx][ny])<=R:
                    city_queue.append((nx, ny))



print(city_queue)



