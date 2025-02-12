import sys

sys.stdin = open("input.txt", "r")

n = int(input())
coin_list = list(map(int, input().split()))
coin_list.sort()
# print(n)
print(coin_list)

target = 1
for i in coin_list:
    if i > target:
        break
    else:
        target+=i
print(target)

