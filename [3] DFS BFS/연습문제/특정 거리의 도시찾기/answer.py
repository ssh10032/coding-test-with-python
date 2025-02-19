import sys
from collections import deque

# input 1 답: 4
# input 2 답: -1
# input 3 답: 2 3
sys.stdin = open("input_3.txt", "r")

# 최단 거리 문제 >> BFS 문제로 접근
# 선입선출 문제, queue를 활용
n, m, k, x = map(int, input().split())

visited = [0]* n

# 각 도시간 도로 연결 정보를 기록하는 행렬
road_matrix = [[0]*n for _ in range(n)]

for _ in range(m):
    sc, ac = map(int, input().split())
    road_matrix[sc-1][ac-1] = 1

queue = deque()
queue.append(x-1)

while queue:
    c_num = queue.popleft()
    for i in range(n):
        if road_matrix[c_num][i]==1:
            queue.append(i)
            # 현재 지점이 시작 지점이 아닐 경우 and bfs 탐색중 첫 방문이 아닌 경우에만
            # >> 최단거리 기록
            if i!=x-1 and visited[i]==0:
                visited[i] = visited[c_num]+1

answer = []

for i in range(len(visited)):
    if visited[i]==k:
        answer.append(i+1)

if not answer:
    print(-1)
elif len(answer)!=1:
    answer.sort()
    print(answer)
else:
    print(answer)









