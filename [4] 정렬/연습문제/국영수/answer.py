import sys

sys.stdin = open("input.txt", "r")

n = int(input())
data_list = []

for _ in range(n):
    input_data = input().split()
    data_list.append((input_data[0], int(input_data[1]), int(input_data[2]), int(input_data[3])))

print(data_list)

data_list = sorted(data_list, key=lambda student:student[1], reverse=True)

# 약한 부분
# sorted 함수의 key 인자에서 정렬 단위를 우선순위 순서대로 여러개로 지정해줄수 있음
# 조건문 여러개 안만들고, 매우 짧게 만들 수 있으니까 기억해두자
for i in range(n):
    for j in range(i+1, len(data_list)):
        if data_list[i][1] == data_list[j][1]:
            if data_list[i][2] > data_list[j][2]:
                data_list[i], data_list[j] = data_list[j], data_list[i]
            elif data_list[i][2]==data_list[j][2]:
                if data_list[i][3] < data_list[j][3]:
                    data_list[i], data_list[j] = data_list[j], data_list[i]
                elif data_list[i][3] == data_list[j][3]:
                    if data_list[i][0] > data_list[j][0]:
                        data_list[i], data_list[j] = data_list[j], data_list[i]

for idx in range(n):
    print(data_list[idx][0])