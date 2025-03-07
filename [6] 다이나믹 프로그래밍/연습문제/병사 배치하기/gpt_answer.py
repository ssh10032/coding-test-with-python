import sys

sys.stdin = open("input.txt", "r")

# 이전까지 기록한 최대 리스트 길이들을
# 반복문을 통해 모두 비교해야함
# 이중 for 문을 쓰기 때문에 이렇게 구현하면
# 시간 복잡도가 O(N*N)임
# 이진 탐색도 같이 넣으면 시간 복잡도를 줄일 수 있다고 함
n = int(sys.stdin.readline().rstrip())
s = list(map(int, sys.stdin.readline().rstrip().split()))

# dp는 내림차순으로 정렬했을 때
# 가장 긴 리스트의 길이를 저장
dp = [1] * n

for i in range(1, n):
    # i 이전 값들
    for j in range(0, i):
        # 이전 값이 현재 값보다 큰 경우
        if s[j] > s[i]:
            # 내림차순을 만족하면
            # 그 인덱스까지 가장 긴 행렬길이 + 1
            # 현재 값
            # 비교해서 가장 큰 값으로 저장
            dp[i] = max(dp[i], dp[j]+1)

lds_length = max(dp)


print(n)
print(s)
print(dp)
print(n-lds_length)