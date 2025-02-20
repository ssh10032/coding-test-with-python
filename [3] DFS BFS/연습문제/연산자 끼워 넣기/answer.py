import sys

sys.stdin = open("input.txt", "r")

n = int(input())

num_list = list(map(int, input().split()))

operator_list = list(map(int, input().split()))

print('')