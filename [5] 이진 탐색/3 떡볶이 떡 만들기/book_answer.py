import sys

sys.stdin = open("input.txt", "r")

n, m = map(int, sys.stdin.readline().rstrip().split())

l_lst = list(map(int, sys.stdin.readline().rstrip().split()))

start = 0
end = max(l_lst)

# (0 ~ max떡 길이) 까지를 탐색 범위로 삼고,
# 탐색 시작 길이를 중간값 (0+max)//2로 설정

# 자르고 목표치보다 작으면

# 0~max를 절반으로 나눈 값을 중간 값으로 설정
result = 0

while(start<=end):
    total = 0
    mid = (start+end)//2

    for x in l_lst:
        if x > mid:
            total+=(x-mid)
    # 자른 떡 길이 총합(total)이 m보다 작으면
    # 많이 자른거니까 >> 더 조금 자르도록
    # 탐색 범위를 (start, mid-1)로 설정
    if total < m:
        end = mid-1
    # 자른 떡 길이 총합(total)이 m보다 크면
    # 일단 만족하니까 result에 저장
    # 좀 더 잘라도 될수도 있으니
    # 다음 탐색 범위를 (mid+1, end)로 설정.
    else:
        result = mid
        start = mid + 1
print(result)