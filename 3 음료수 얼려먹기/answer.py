import sys
from collections import deque

def bfs(in_matrix, visited, x, y):
    visited[x][y] = True
    queue = deque((x ,y))

    while all(visited):
        x, y = queue.popleft()
        print('check')


sys.stdin = open("input.txt", "r")

# 구멍이 뚫려있는 부분은 0, 칸막이가 설치되어있는 부분은 1
# 틀의 모양이 주어졌을 때, 생성되는 아이스크림의 총 수를 구하시오
in_matrix = [list(map(int, input().split())) for _ in range(4)]

print(in_matrix)

print(len(in_matrix[0]))
print(len(in_matrix))

visited = [[False] * len(in_matrix[0])] * len(in_matrix)
print(visited)

bfs(in_matrix, visited, 0, 0)