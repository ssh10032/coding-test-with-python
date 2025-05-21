# 가장 작은 데이터를 선택해 맨앞 데이터와 바꾸고
# 그 다음 작은 데이터를 선택해 앞에서 두 번째 데이터와 바꾸는 방식
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

print(array)

# 연산 횟수는 N + (N-1) + (N-2) ... + 2
# >> 근사치로 N * (N+1) / 2 번의 연산 수행
# 빅오 표기법으로 O(N**2)

# 데이터 개수가 100개 늘면, 연산량은 10,000배 늘어나버림
# >> 데이터 개수 늘면 느려짐