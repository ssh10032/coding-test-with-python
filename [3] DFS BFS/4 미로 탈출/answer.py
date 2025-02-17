import sys
from collections import deque

def bfs(graph, x, y, visited):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    print('check')

    while queue:
        x, y = queue.popleft()
        if x + 1 >=0 and x+1<n:
            if not visited[x+1][y] and graph[x+1][y]==1:
                queue.append((x+1, y))
        if x -1 >= 0 and x-1 < n:
            if not visited[x-1][y]:
                queue.append((x-1, y))
        if y-1>=0 and y-1<n:
            if not visited[x][y-1]:
                queue.append((x, y-1))
        if y+1>=0 and y+1<n:
            if not visited[x][y+1]:
                queue.append((x, y+1))


        print('check')




# bfs로 구현, deque 사용
sys.stdin = open("input.txt", "r")

# 처음 위치 좌표 (1, 1)
# 미로의 출구는 (n, m)에 위치함
n, m = map(int, input().split())

# 괴물이 있는 곳은 0, 없는 곳은 1
# 탈출하기 위해 움직여야하는 최소 칸의 개수를 출력
maze = []
for _ in range(n):
    maze.append(list(map(int, input())))

visited = [[False] * n] * m
print(visited)
print(maze)
bfs(0,0)