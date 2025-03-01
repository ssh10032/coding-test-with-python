import sys

sys.stdin = open("input_5.txt", "r")

def binary_search_dist(home, start, end, h_num):
    h_num-=2
    if h_num==0:
        return home[end]-home[start]
    while start <= end:
        mid = (start+end)//2
        if h_num==1:
            if home[mid]-home[start]>home[end]-home[mid]:
                dist = home[end]-home[mid]
            else:
                dist = (home[mid]-home[start])
            h_num-=1
            return dist
        else:
            if home[mid] - home[start] > home[end] - home[mid]:
                end = mid-1
            else:
                start = mid+1
            h_num-=1
    return None

# n : 집의 개수, m : 설치할 수 있는 공유기 수
n, m = map(int, sys.stdin.readline().rstrip().split())
# 집의 좌표들
home = []
for _ in range(n):
    # h = int(input())
    h = int(sys.stdin.readline().rstrip())
    home.append(h)

home.sort()

# 가장 인접한 두 공유기 사이의 거리가 최대로 되도록 배치

print(binary_search_dist(home, 0, n-1, m))
