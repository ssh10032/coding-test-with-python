import sys
# input 1 답 : 5
# input 2 답 : 10
# input 3 답 : 11
sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())

n_list = [list(map(int, input().split())) for _ in range(n)]

# 0은 빈칸, 1은 집, 2는 치킨집
# 치킨 거리 : 집에서 가장 가까운 치킨 집까지의 거리를 뜻함

# 도시의 치킨 거리 = 모든 집의 치킨 거리의 합
# m은 고를 수 있는 치킨 집 수
print(n)
print(m)
print(n_list)

h_list = []
c_list = []
min_list = []

for i in range(n):
    for j in range(n):
        if n_list[i][j]==1:
            h_list.append([i, j])
        elif n_list[i][j]==2:
            c_list.append([i, j])
print(h_list)
print(c_list)

for x, y in h_list:
    min_dist = (n-1)*2
    for cx, cy in c_list:
        dist = abs((cx-x)+(cy-y))
        if dist<min_dist:
            min_dist = dist
            min_x = cx
            min_y = cy
    min_list.append([min_x, min_y])

min_list = set(min_list)
print(min_list)
