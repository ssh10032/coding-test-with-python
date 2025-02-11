import sys

sys.stdin = open("input.txt", "r")

n, k = map(int, input().split())

result = 0

while True:
    # target = n에서 1씩 빼서 만들어야할 K의 배수
    target = (n//k) * k
    # result = n에서 1을 빼야할 횟수
    result += (n-target)
    n = target

    # K의 배수로 더이상 만들 수 없으면 break
    if n < k:
        break

    # k의 배수로 만들 수 있으면 나누고, result +1
    result +=1
    n //= k

# 마지막 남은 수 n 에서 1을 뺄 횟수 (n-1) 더하기
result += (n-1)
print(result)