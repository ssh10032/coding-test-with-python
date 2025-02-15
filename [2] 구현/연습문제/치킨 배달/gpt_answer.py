import sys
# 전체 치킨 집에서 M개를 조합
### 부족했던 점 : 완전 탐색 문제에서 조합을 위한 라이브러리 사용 ####
# 라이브러리 사용
# combinations(list, M)을 호출하면
# list 중에 M개를 선택해 조합한 리스트들을 반환해줌
from itertools import combinations

def get_city_chicken_dist(houses, selected_chickens):
    total_dist = 0
    for hx, hy in houses:
        min_dist = float('inf')
        for cx, cy in selected_chickens:
            min_dist = min(min_dist, abs(hx-cx)+abs(hy-cy))
        total_dist += min_dist
    return total_dist

# input 1 답 : 5
# input 2 답 : 10
# input 3 답 : 11
# input 4 답 : 32
sys.stdin = open("input_4.txt", "r")

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

houses = []
chickens = []

for r in range(N):
    for c in range(N):
        if city[r][c]==1:
            houses.append((r, c))
        elif city[r][c]==2:
            chickens.append((r, c))

min_chicken_dist = float('inf')

for selected_chickens in combinations(chickens, M):
    city_chicken_distance = get_city_chicken_dist(houses, selected_chickens)
    min_chicken_dist = min(min_chicken_dist, city_chicken_distance)

print(min_chicken_dist)