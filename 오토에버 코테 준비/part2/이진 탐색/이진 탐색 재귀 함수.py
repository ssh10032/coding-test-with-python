import sys

sys.stdin = open("input.txt", "r")

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2
    if array[mid] == target:
        return mid
    elif array[mid]>target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

n, target = list(map(int, sys.stdin.readline().rstrip().split()))
array = list(map(int, sys.stdin.readline().rstrip().split()))

result = binary_search(array, target, 0, n-1)

if result==None:
    print("no exist")
else:
    print(result+1)
