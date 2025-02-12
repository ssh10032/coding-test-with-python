import sys

sys.stdin = open("input.txt", "r")

adventure_list = list(map(int, input().split()))

# list 오름차순으로 정렬
adventure_list.sort()

# 그룹 수
result = 0
# 그룹 인원 수
n = 1

for i in adventure_list:
    if n >= i:
        result+=1
        n = 1
    else :
        n+=1

print(result)
