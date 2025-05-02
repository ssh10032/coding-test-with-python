import sys

sys.stdin = open("input_3.txt", "r")

n = int(sys.stdin.readline().rstrip())

n_list = list(map(int, sys.stdin.readline().rstrip().split()))
add, sub, mul, div = map(int, sys.stdin.readline().rstrip().split())

min_value = 1e9
max_value = -1e9

def dfs(i, now):
    global min_value, max_value, add, sub, mul, div
    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)

    else:
        if add > 0:
            add-=1
            dfs(i+1, now+n_list[i])
            add+=1
        if sub > 0:
            sub-=1
            dfs(i+1, now-n_list[i])
            sub+=1
        if mul > 0:
            mul-=1
            dfs(i+1, now*n_list[i])
            mul+=1
        if div > 0:
            div-=1
            dfs(i+1, int(now/n_list[i]))
            div+=1

dfs(1, n_list[0])

print(max_value)
print(min_value)