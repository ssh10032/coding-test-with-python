array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


# 연산 횟수 = N + (N-1) + (N-2) + (N-3) + ... + 2
# >> 근사치 : N * (N+1) / 2 번의 연산
# >> 빅오 표기법 O(N*N)
# 데이터 개수가 10000개 이상이면, 정렬 속도가 급격하게 느려짐
# 매우 비효율적
for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

print(array)