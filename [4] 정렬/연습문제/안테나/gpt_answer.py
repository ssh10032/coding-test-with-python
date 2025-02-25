import sys

sys.stdin = open("input.txt", "r")

n = int(input())

home_lst = list(map(int, input().split()))

# 거리의 최솟값은 항상 중앙 인덱스 값이 되는 것이 맞음
def antena_dist(n, home_lst):
    home_lst.sort()
    mid_idx = (n-1)//2

    return home_lst[mid_idx]

print(antena_dist(n, home_lst))