import sys

sys.stdin = open("input.txt", "r")

# 다이나믹 프로그래밍의 핵심
# 점화식을 만들 수 있는 조건을 먼저 파악하고, 코드로 만들어줘야함!!
# 피보나치 만드는 것 처럼
# d(0), d(1) >> 점화식을 시작하기 위한
# 점화에 필요한 요소가 뭔지 파악해야함!!!!

n = int(sys.stdin.readline().rstrip())
array = list(map(int, sys.stdin.readline().rstrip().split()))

d = [0] * 100

d[0] = array[0]
d[1] = max(array[0], array[1])

# 그 다음 리스트는
# 1. 그 전 요소까지 더한 경우
# 2. 그전전 요소까지 더한 것 + 현재 요소 더한 것
# 중에 가장 큰 것으로 설정
# 결과적으로 n-1번째 요소에는 최댓값이 기록되게 됨!!

for i in range(2, n):
    d[i] = max(d[i-1], d[i-2]+array[i])

print(d[n-1])