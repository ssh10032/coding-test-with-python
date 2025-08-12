import sys

sys.stdin = open("input.txt", "r")

num_list = str(sys.stdin.readline().rstrip())
num_list = list(int(i) for i in num_list)
num_list.sort()

result = 0

for i in num_list:
    if result==0:
        result+=i
    else:
        result*=i

print(result)
