import sys
# input 1 : 3
# input 2 : 2
# input 3 : -1
sys.stdin = open("input_3.txt", "r")
# 고정점 = 인덱스와 값이 같은 경우
def binary_search(n_list, start, end):
    while start<=end:
        mid = (start+end)//2
        if n_list[mid]==mid:
            return mid
        elif n_list[mid]>mid:
            return binary_search(n_list, start, mid-1)
        else:
            return binary_search(n_list, mid+1, end)
    return None

# n = int(input())
# n_lst = list(map(int, input().split()))

n = int(sys.stdin.readline().rstrip())
n_lst = list(map(int, sys.stdin.readline().rstrip().split()))

print(n)
print(n_lst)

result = binary_search(n_lst, 0, n-1)

if result == None:
    print(-1)
else:
    print(result)