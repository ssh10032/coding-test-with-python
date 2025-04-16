import sys

sys.stdin = open("input.txt", "r")

# 00시 00분 ~ N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램
n = int(sys.stdin.readline().rstrip())

result = 0
min_sec = 0
for i in range(60):
    for j in range(60):
        if "3" in str(i) or "3" in str(j):
            min_sec+=1

for i in range(0, n+1):
    if "3" in str(i):
        result+=3600
    else:
        result+=min_sec

print(result)

