import sys
sys.stdin = open("input.txt", "r")

# 공백을 구분하여 3개 정수 입력 받기
n, m, k = map(int, input().split())

# 공백을 구분하여 정수들을 리스트로 입력 받기
data = list(map(int, input().split()))

# 리스트 오름 차순으로 정렬
data.sort()
# 가장 큰 수
first = data[n-1]
# 가장 작은 수
second = data[n-2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0 :
        break
    result += second
    m -= 1

print(result)
