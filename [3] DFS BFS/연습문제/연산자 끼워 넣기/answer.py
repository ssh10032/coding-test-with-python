# DFS/BFS
# DFS는 stack(FILO), 재귀 호출
# BFS는 deque(FIFO), 반복문
import sys
from collections import deque
from itertools import combinations

sys.stdin = open("input_2.txt", "r")

n = int(input())

# value 0 : 더하기, 1 : 빼기, 2 : 곱하기, 3 : 나누기
op_lst = [0] * (n-1)

num_list = deque(list(map(int, input().split())))

# 순서대로 +, -, x, //
operator_list = deque(list(map(int, input().split())))





# def bfs


print(n)
print(num_list)
print(operator_list)
print('')