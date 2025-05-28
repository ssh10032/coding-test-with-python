array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# sorted는 새로운 변수에 정렬된 리스트 할당
result = sorted(array)
print(result)

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# sort는 원본 리스트를 정렬
array.sort()
print(array)

# key를 매개변수로 받는 정렬
array = [('바나나',2),('사과',5),('당근',3)]

def setting(data):
    return data[1]
result = sorted(array, key=setting)

print(result)