import sys

sys.stdin = open("input_2.txt", "r")

def check_count(n, target, n_lst):
    count = 0
    for i in range(n):
        if n_lst[i] == m:
            count += 1
    if count == 0:
        return -1
    return count

n, m = map(int, sys.stdin.readline().rstrip().split())

n_lst = list(map(int, sys.stdin.readline().rstrip().split()))

print(check_count(n, m, n_lst))