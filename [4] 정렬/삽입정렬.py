# 삽입 정렬의 시간 복잡도 : O(N*N)
# 현재 리스트의 데이터가 거의 정렬되어 있는 경우, 매우 빠르게 동작함
# 최선의 경우 O(N)의 시간 복잡도를 가짐

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
print(array)
for i in range(1, len(array)):
    print('idx is ', i)
    # range의 매개변수는 3개 (start, end, step)
    # step에 -1이 들어가면, start 인덱스부터 시작해서 end+1 인덱스까지 1씩 감소.
    for j in range(i, 0, -1): # 인덱스 i부터 1까지 감소하며 반복하는 문법

        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
            print(array)
        else:
            print(array)
            break