# 찾고자하는 요소를 순차적으로 탐색
def sequantial_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i+1

print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.")

# input_data = input().split()
# n = int(input_data[0])
# target = input_data[1]
n = 5
target = "Dongbin"

print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")
# array = input().split()
array = "Hanul Jonggu Dongbin Taeil Sangwook"
array = array.split()

print(sequantial_search(n, target, array))