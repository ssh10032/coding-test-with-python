import sys

sys.stdin = open("input_2.txt", "r")

n, m = map(int, input().split())
ball_list = list(map(int, input().split()))
ball_list.sort()

result = 0
for idx, i in enumerate(ball_list):
    target = i
    for j in ball_list[idx+1:]:
        if j!= target:
            result+=1
print(result)