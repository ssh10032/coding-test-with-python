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
            # print(f'{array[mid]} is bigger than {target}'.format())
            return binary_search(array, target, start, mid-1)
        else:
            # print(f'{array[mid]} is smaller than {target}'.format())
            return binary_search(array, target, mid+1, end)


n = int(sys.stdin.readline().rstrip())

# n_lst = sys.stdin.readline().rstrip()
# n_lst = list(map(int, input().split()))
n_lst = list(map(int, sys.stdin.readline().rstrip().split()))

m = int(sys.stdin.readline().rstrip())
m_lst = list(map(int, sys.stdin.readline().rstrip().split()))

n_lst.sort()
# print(n_lst)


for target in m_lst:
    result = binary_search(n_lst, target, 0, n-1)
    if result == None:
        print("No", end=' ')
    else:
        print("Yes", end=' ')