import sys

# 완전 탐색 >>
# sys.stdin = open("input.txt", "r")
# sys.stdin = open("input_2.txt", "r")
sys.stdin = open("input_3.txt", "r")

n = int(input())

n_list = list(map(int, input().split()))

opr_list = list(map(int, input().split()))

mx = -1e9
mn = 1e9

def dfs(depth, temp):
    global mx, mn

    if depth == n-1:
        mx = max(temp, mx)
        mn = min(temp, mn)
        return

    if opr_list[0]!=0:
        opr_list[0]-=1
        dfs(depth+1, temp + n_list[depth+1])
        opr_list[0]+=1

    if opr_list[1]!=0:
        opr_list[1]-=1
        dfs(depth+1, temp - n_list[depth+1])
        opr_list[1]+=1

    if opr_list[2]!=0:
        opr_list[2]-=1
        dfs(depth+1, temp * n_list[depth+1])
        opr_list[2]+=1

    if opr_list[3]!=0:
        opr_list[3]-=1
        dfs(depth+1, int(temp / n_list[depth+1]))
        opr_list[3]+=1

dfs(0, n_list[0])

print(mx)
print(mn)



