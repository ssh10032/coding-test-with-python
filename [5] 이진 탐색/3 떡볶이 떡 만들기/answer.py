import sys

def binary_search(array, target, start, end):
    if start > end:
        if 0<=start<len(array):
            return sum(i-target for i in array[start:])
        else:
            return 0
        print('start is ',start)
        print('end is ', end)
        return None
    else:
        mid = (start + end)//2
        if array[mid]==target:
            return sum(i-target for i in array[mid:])
            # return mid
        # 중간값이 target보다 큰 경우, 왼쪽에서 다시 탐색
        elif array[mid]>target:
            return binary_search(array, target, start, mid-1)
        # 중간값이 target보다 작은 경우, 오른쪽에서 다시 탐색
        else:
            return binary_search(array, target, mid+1, end)

sys.stdin = open("input.txt", "r")

# 떡을 ncm로 잘랐을때, 적어도 mcm를 챙길수 있어야함..
# m의 최댓값
n, m = map(int, sys.stdin.readline().rstrip().split())

l_lst = list(map(int, sys.stdin.readline().rstrip().split()))

l_lst.sort()

print(l_lst)

start_target = 0
end_target = max(l_lst)

for i in range(end_target, start_target-1, -1):
    result = binary_search(l_lst, i, 0, n-1)
    if result >=m:
        print(i)
        break




# print(binary_search(l_lst, 11, 0, n-1))
# print(binary_search(l_lst, 13, 0, n-1))
#
# print(binary_search(l_lst, 18, 0, n-1))
# print(binary_search(l_lst, 20, 0, n-1))