import sys

# 이진 탐색 코드 암기하면 도움이 되는 경우가 많음. 암기해두자
# 탐색 범위가 2000만을 넘어가면 이진 탐색으로 접근해보자

# 데이터 수나 값이 1000만 단위 이상으로 넘어가면
# 이진 탐색과 같이 O(logN)의 속도를 내는 알고리즘을 떠올려야함
sys.stdin = open("input.txt", "r")

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

# n(원소의 개수)과 target(찾고자 하는 문자열) 입력받기
n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)

if result == None:
    print("원소가 존재하지 않습니다")
else:
    print(result+1)