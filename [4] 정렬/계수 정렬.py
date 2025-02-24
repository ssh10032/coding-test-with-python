# 계수 정렬의 시간 복잡도
# 데이터 개수를 N, 데이터 최대값의 크기를 K
# 시간 복잡도 O(N + K)

array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

count = [0] * (max(array)+1)

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')