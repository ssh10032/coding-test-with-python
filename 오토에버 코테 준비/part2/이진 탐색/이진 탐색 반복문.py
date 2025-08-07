import sys

sys.stdin = open("input.txt", "r")

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if array[mid]==target:
            return mid
        elif array[mid]>target:
            end = mid-1
        else:
            start = mid+1
    return None


n, target = map(int, sys.stdin.readline().rstrip().split())

array = list(map(int, sys.stdin.readline().rstrip().split()))

result = binary_search(array, target, 0, n-1)