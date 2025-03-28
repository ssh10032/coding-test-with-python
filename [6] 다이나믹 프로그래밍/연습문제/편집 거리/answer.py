import sys

sys.stdin = open("input2.txt", "r")

astr = str(sys.stdin.readline().rstrip())
bstr = str(sys.stdin.readline().rstrip())

print(astr)
print(bstr)

# dp 초기화
dp = [[0] * (len(bstr)+1) for _ in range(len(astr)+1)]
for i in range(1, len(bstr)+1):
    dp[0][i] = i
for j in range(1, len(astr)+1):
    dp[j][0] = j
print(dp)

# astr[row], bstr[col] 비교
# 1 같은 경우
# dp[row-1][col-1]을 그대로 가져옴
# 2 다른 경우
# 삽입 : dp[row-1][col]+1
# 삭제 : dp[row][col-1]+1
# 수정 : dp[row-1][col-1]+1
for i in range(1, len(astr)+1):
    for j in range(1, len(bstr)+1):
        if astr[i-1] == bstr[j-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])+1

print(dp[len(astr)][len(bstr)])