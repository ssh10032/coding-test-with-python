import sys

sys.stdin = open("input.txt", "r")

def binary_search(array, target, start, end):
    if start > end:
        return None
    else:
        mid = (start + end)//2
        if array[mid]==target:
            return mid
        elif array[mid]>target:
            return binary_search(array, target, start, mid-1)
        else:
            return binary_search(array, target, mid+1, end)

n = int(sys.stdin.readline().rstrip())

array = list(map(int, sys.stdin.readline().rstrip().split()))
array.sort()

m = int(sys.stdin.readline().rstrip())

x = list(map(int, sys.stdin.readline().rstrip().split()))

for i in x:
    result = binary_search(array, i, 0, n-1)
    if result !=None:
        print('yes', end=' ')
    else:
        print('no', end=' ')