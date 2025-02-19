import sys

# input 1 answer: 27
# input 2 answer: 9
# input 3 answer: 3

# 0은 빈칸, 1은 벽, 2는 바이러스
# 새로 세울 수 있는 벽은 3개, 모두 세워야함
# 벽을 세워서 만들 수 있는 안전지대의 최대 넓이를 구해야함

# dfs 재귀 호출, 스택을 사용 선입 후출
def dfs(graph, wall_num, v_idx):
    print('dfs algorithm')
    dfs(graph, wall_num)



sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
graph = []
wall_num = 3
for _ in range(n):
    graph.append(list(map(int, input().split())))

print(graph)
v_idx = []
for i in range(n):
    for j in range(n):
        if graph[i][j]==2:
            v_idx.append([i, j])

print(v_idx)

dfs(graph, wall_num, v_idx)