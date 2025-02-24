# sorted 라이브러리를 활용한 정렬
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# sorted의 경우, 별도로 정렬된 리스트가 반환되어 새로운 변수에 할당해야함
result = sorted(array)

print(result)

# sort 라이브러리를 활용한 정렬
array_2 = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# sort()의 경우 내부 원소가 바로 정렬됨
array_2.sort()

print(array_2)

array_3 = [('바나나', 2), ('사과', 5), ('당근', 3)]

def setting(data):
    return data[1]

result = sorted(array_3, key=setting)
print(result)