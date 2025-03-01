import sys

sys.stdin = open("input.txt", "r")

# 거리가 dist일 때 공유기 c개를 설치할 수 있는지 확인
def can_place_routers(home, dist, c):
    count = 1
    last_position = home[0]

    for i in range(1, len(home)):
        if home[i]-last_position >= dist:
            count+=1
            last_position = home[i]
            if count >= c:
                return True
    return False

# 이분 탐색을 사용하여 공유기 사이의 최대 거리 찾기
def binary_search_max_dist(home, c):
    # left : 공유기 간 최소 거리
    # right : 공유기 간 최대 거리(양쪽 끝 집 사이의 거리)
    left = 1
    right = home[-1]-home[0]
    result = 0

    while left <= right:
        # 공유기 최소/최대 거리의 중간 값
        mid = (left+right)//2

        # 중간 값을 간격으로 c개의 공유기를 설치할 수 있는지 체크
        if can_place_routers(home, mid, c):
            # 가능한 경우, result에 값 저장후
            # 더 큰 거리로 가능한지 체크
            result = mid
            left = mid+1
        else:
            right = mid-1
    return result


n, m = map(int, sys.stdin.readline().rstrip().split())

print(n)
print(m)

home = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
home.sort()

print(home)
print(binary_search_max_dist(home, m))