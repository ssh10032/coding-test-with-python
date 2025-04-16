import sys

sys.stdin = open("input.txt", "r")

# n이 1이 될 때 까지 반복
#1 n에서 1을 뺀다
#2 n을 k로 나눈다(n이 k로 나누어 떨어질때만 선택 가능)

n, k = map(int, sys.stdin.readline().rstrip().split())

result = 0

while True:
    if n == 1:
        break
    if n%k==0:
        n = n//k
    else:
        n-=1
    result+=1

print(result)