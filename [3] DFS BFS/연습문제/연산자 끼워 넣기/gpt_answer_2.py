import sys

# sys.stdin = open("input.txt", "r")
sys.stdin = open("input_2.txt", "r")
# sys.stdin = open("input_3.txt", "r")

n = int(input())

num_list = list(map(int, input().split()))

plus, minus, multiply, devide = map(int, input().split())
# opr_list = list(map(int, input().split()))

max_value = -1e9
min_value = 1e9

def dfs(depth, result, plus, minus, multiply, devide):
    global max_value, min_value
    if depth == n:
        max_value = max(max_value, result)
        min_value = min(min_value, result)
        return

    if plus:
        dfs(depth+1, result + num_list[depth], plus-1, minus, multiply, devide)
    if minus:
        dfs(depth+1, result - num_list[depth], plus, minus-1, multiply, devide)
    if multiply:
        dfs(depth+1, result * num_list[depth], plus, minus, multiply-1, devide)
    if devide:
        dfs(depth+1, result * num_list[depth], plus, minus, multiply, devide-1)



dfs(1, num_list[0], plus, minus, multiply, devide)

print(max_value)
print(min_value)