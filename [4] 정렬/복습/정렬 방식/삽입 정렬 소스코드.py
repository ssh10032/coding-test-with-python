array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(array)):
    # i부터 1까지 감소하면서 탐색
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break

print(array)
# 이중 for문으로
# 삽입 정렬도 시간 복잡도는 O(N**2)
# 리스트가 거의 정렬되어 있는 경우에는 빠르게 동작