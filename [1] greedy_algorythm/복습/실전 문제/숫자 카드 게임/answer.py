import sys

sys.stdin = open("input2.txt", "r")

n, m = map(int, sys.stdin.readline().rstrip().split())

min_list = []
result = 0
for _ in range(n):
   num_list = list(map(int, sys.stdin.readline().rstrip().split()))
   num_list.sort()
   if num_list[0]>result:
       result = num_list[0]

print(result)
