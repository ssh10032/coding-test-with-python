# 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 정렬

# 피벗을 사용
# 피벗 : 큰 숫자와 작은 숫자를 교환할 때, 교환하기 위한 '기준'을 피벗이라고 함

array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
    # 리스트의 원소가 1개인 이유
    if start>=end:
        return
    pivot = start
    left = start+1
    right = end
    while left<=right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left<=end and array[left]<=array[pivot]:
            left+=1
        while right > start and array[right]>=array[pivot]:
            right-=1
        # 엇갈린 경우
        if left>right:
            # 피벗보다 작은 데이터를 피벗과 위치 교체
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    # 분할한 이후로 왼쪽 부분과 오른쪽 부분에 대해 각각 정렬 수행
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)

print(array)

# 퀵 정렬의 시간 복잡도는 O(N*logN)
# 삽입 정렬, 선택 정렬보다 빠른 편임

# 피벗을 정하고 데이터를 반띵하고 정렬하는 과정을 반복하니까
# 데이터 수가 N개일 경우, 높이는 log N이라고 할 수 있음(여기서 log는 밑이 2인 로그를 의미함)
# 예시 )) 데이터 수가 8개면 8 > 4 > 2> 1로 분할이 3번 이루어질거라고 생각할 수 있음