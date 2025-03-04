import sys

sys.stdin = open("input.txt", "r")

n = int(sys.stdin.readline().rstrip())

n_list = list(map(int, sys.stdin.readline().rstrip().split()))

print(n)
print(n_list)

food = [0] * n
food[0] = n_list[0]
food[1] = max(n_list[0], n_list[1])

for i in range(2, n):
    food[i] = max(food[i-1], food[i-2]+n_list[i])

print(food[n-1])