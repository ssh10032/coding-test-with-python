import sys

sys.stdin = open("input.txt", "r")

def sequential_search(n, target, array):
    for i in range(n):
        if array[i]== target:
            return i+1

input_data = sys.stdin.readline().rstrip().split()

n = int(input_data[0])
target = input_data[1]

array = sys.stdin.readline().rstrip().split()

print(sequential_search(n, target, array))