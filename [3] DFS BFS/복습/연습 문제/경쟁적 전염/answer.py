import sys

sys.stdin = open("input.txt", "r")

n, m = map(int, sys.stdin.readline().rstrip().split())

graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

print(graph)