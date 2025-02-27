import sys

# 이진 탐색 알고리즘은 데이터 리스트가 정렬되어있는 경우에 사용할 수 있음
def binary_search(array, target, start, end):
    if start > end :
        return None
    # 소수점은 버림
    mid = (start + end)//2

    # 찾는 원소가 중간 값인 경우 그대로 반환
    if array[mid] == target:
        return mid

    # 찾는 원소가 중간 값보다 작은 경우
    elif array[mid]>target:
        # 끝 인덱스를 (중간값-1)로 변경해서 재귀 호출
        return binary_search(array, target, start, mid-1)
    # 찾는 원소가 중간 값보다 큰 경우
    else:
        # 시작 인덱스를 (중간값+1)로 변경해서 재귀 호출
        return binary_search(array, target, mid+1, end)

sys.stdin = open("input_2.txt", "r")

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)

if result==None:
    print("원소가 존재하지 않습니다.")
else:
    print(result+1)