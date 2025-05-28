import sys

sys.stdin = open("input.txt", "r")

n = int(sys.stdin.readline().rstrip())

print(n)

num_list = []
for _ in range(n):
    num_list.append(int(sys.stdin.readline().rstrip()))

print(num_list)

num_list.sort(reverse=True)

print(num_list)

result = sorted(num_list, reverse=True)

print(result)