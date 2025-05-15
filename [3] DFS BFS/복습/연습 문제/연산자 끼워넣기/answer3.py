import sys

# 숫자 사이에 연산자 집어넣기
# 모든 연산 경우의 수에서
# 최대값, 최소값 출력
sys.stdin = open("input_3.txt", "r")

n = int(sys.stdin.readline().rstrip())

num_lst = list(map(int, sys.stdin.readline().rstrip().split()))

# +, -, *, //
opr_lst = list(map(int, sys.stdin.readline().rstrip().split()))


print(n)
print(num_lst)
print(opr_lst)
max_value = -1e9
min_value = 1e9

def dfs(result, idx):
    global max_value, min_value
    if idx == n-1:
        max_value = max(result, max_value)
        min_value = min(result, min_value)
        return
    for i in range(4):
        if i == 0 and opr_lst[i]!=0:
            opr_lst[i]-=1
            dfs(result+num_lst[idx+1], idx+1)
            opr_lst[i]+=1
        elif i == 1 and opr_lst[i]!=0:
            opr_lst[i] -= 1
            dfs(result - num_lst[idx + 1], idx + 1)
            opr_lst[i] += 1
        elif i == 2 and opr_lst[i]!=0:
            opr_lst[i] -= 1
            dfs(result * num_lst[idx + 1], idx + 1)
            opr_lst[i] += 1
        elif i==3 and opr_lst[i]!=0:
            opr_lst[i] -= 1
            dfs(int(result / num_lst[idx + 1]), idx + 1)
            opr_lst[i] += 1

dfs(num_lst[0], 0)

print(max_value)
print(min_value)
