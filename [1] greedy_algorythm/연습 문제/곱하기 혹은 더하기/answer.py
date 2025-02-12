import sys

sys.stdin = open("input_2.txt", "r")

num_list = str(input())
num_list = [int(i) for i in num_list]
num_list.sort()
# print(num_list)
result = 0

for i in num_list:
    if result == 0:
        result += i
    else :
        result *= i

print(result)

