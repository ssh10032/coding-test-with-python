import sys

sys.stdin = open("input.txt", "r")

n = int(sys.stdin.readline().rstrip())

q = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

dp = [0] * (n+1)

print(q)

for i in range(n):
    if i + q[i][0]<=n:
        dp[i + q[i][0]] = max(dp[i + q[i][0]], dp[i] + q[i][1])

    dp[i+1] = max(dp[i+1], dp[i])

print(dp)
print(dp[n])