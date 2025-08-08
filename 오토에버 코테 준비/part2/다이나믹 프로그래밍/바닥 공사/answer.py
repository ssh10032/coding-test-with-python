import sys

sys.stdin = open("input.txt", "r")
# n * 2 크기의 타일
# 1 * 2, 2 * 1, 2 * 2의 덮개로 채우고자함
# 바닥을 채우는 모든 경우의 수를 구하는 프로그램 작성
n = int(sys.stdin.readline().rstrip())

d= [0] * 1001

d[1] = 1
d[2] = 3

for i in range(3, n+1):
    d[i] = (d[i-1]+ 2 * d[i-2]) % 796796

print(d[n])