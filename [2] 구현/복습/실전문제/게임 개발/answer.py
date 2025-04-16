import sys

sys.stdin = open("input.txt", "r")

n, m = map(int, sys.stdin.readline().rstrip().split())

# 보고 있는 방향
# 북 : 0
# 동 : 1
# 남 : 2
# 서 : 3
a, b, d = map(int, sys.stdin.readline().rstrip().split())
direction = [0, 3, 2, 1]
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
# 지도에서
# 육지 : 0
# 바다 : 1
matrix = []
visited = [[0] * m for _ in range(n)]

visited[a][b]=1

for _ in range(n):
    num_list = list(map(int, sys.stdin.readline().rstrip().split()))
    matrix.append(num_list)

# print(visited)
# print(matrix)
while True:
    for i in range(len(direction)):
        if d == direction[i]:
            for j in range(1, len(direction)+1):
                next_idx = (i+j)%4
                nx = a + dx[next_idx]
                ny = b + dy[next_idx]
                if 0<nx<=m and 0<ny<=n:
                    if matrix[nx][ny]==0 and visited[nx][ny]==0:
                        a = nx
                        b = ny
                        visited[a][b]=1
                    else:






