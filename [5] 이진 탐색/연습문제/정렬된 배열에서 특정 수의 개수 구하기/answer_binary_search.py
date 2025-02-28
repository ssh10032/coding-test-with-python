import sys

# 재귀 호출로 구현한 이진 탐색
def binary_search(n_lst, target,start, end):
    if start > end:
        return None
    mid = (start + end)//2
    if n_lst[mid] == target:
        return mid
    elif n_lst[mid] > target:
        return binary_search(n_lst, target, start, mid-1)
    else:
        return binary_search(n_lst, target, mid+1, end)

# 반복문으로 구현한 이진 탐색
def binary_search_for(n_lst, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if n_lst[mid] == target:
            return mid
        elif n_lst[mid] > m:
            end = mid - 1
        else:
            start = mid + 1
    return None

# 이진 탐색을 활용한 첫번쨰 인덱스 탐색
def binary_search_start(n_lst, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if n_lst[mid]==target:
            if n_lst[mid-1]!=target:
                return mid
            else:
                end = mid-1
        elif n_lst[mid]>m:
            end = mid-1
        else:
            start = mid+1
    return None
# 이진 탐색을 활용한 마지막 인덱스 탐색
def binary_search_end(n_lst, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if n_lst[mid]==target:
            if n_lst[mid+1]!=target:
                return mid
            else:
                start = mid+1
        elif n_lst[mid]>m:
            end = mid - 1
        else:
            start = mid + 1
    return None

sys.stdin = open("input.txt", "r")

n, m = map(int, sys.stdin.readline().rstrip().split())

n_lst = list(map(int, sys.stdin.readline().rstrip().split()))

# print(n)
# print(m)
#
# print(n_lst)
# print(binary_search(n_lst, m, 0, n-1))
# print(binary_search_for(n_lst, m, 0, n-1))
start_idx = binary_search_start(n_lst, m, 0, n-1)
end_idx = binary_search_end(n_lst, m, 0, n-1)
if start_idx is None or end_idx is None:
    print(-1)
else:
    print(end_idx-start_idx+1)