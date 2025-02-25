import sys

sys.stdin = open("input.txt", "r")

n = int(input())

home_lst = list(map(int, input().split()))

mn_home = min(home_lst)
mx_home = max(home_lst)

# 정렬 문제인데 정렬로 안풀었음
def antena_dist(home_lst, mn_home, mx_home):
    min_dist = 200000
    min_idx = 0
    for i in range(mn_home, mx_home+1):
        total_dist = 0
        for j in home_lst:
            total_dist += abs(i-j)
        if total_dist < min_dist:
            min_dist = total_dist
            min_idx = i
    return min_idx

print(antena_dist(home_lst, mn_home, mx_home))

