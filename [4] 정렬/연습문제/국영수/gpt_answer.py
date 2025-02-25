import sys

sys.stdin = open("input.txt", "r")

n = int(input())

student_list = []


for _ in range(n):
    input_data = input().split()
    student_list.append((input_data[0], int(input_data[1]), int(input_data[2]), int(input_data[3])))

print(student_list)
# print(student_list.sort())
def sort_student(std_list):
    # - 붙이면 내림차순, +면 오름차순
    std_list.sort(key=lambda std:(-std[1], std[2], -std[3], std[0]))
    # std_list = sorted(std_list, key=lambda std:(-std[1], std[2], -std[3],std[0]))
    return std_list

print(sort_student(student_list))
