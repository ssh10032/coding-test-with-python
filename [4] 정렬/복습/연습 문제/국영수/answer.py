import sys

#1 국어 점수 감소하는 순서
#2 국어 점수가 같으면 영어 점수가 증가하는 순서
#3 국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서
#4 모든 점수가 같으면 사전 순으로 중가하는 순서로

sys.stdin = open("input.txt", "r")

n = int(sys.stdin.readline().rstrip())

score_list = []

for _ in range(n):
    name, s1, s2, s3 = map(str, sys.stdin.readline().rstrip().split())
    score_list.append((name, int(s1), int(s2), int(s3)))

print(score_list)

# score_list.sort(reverse=True, key=lambda a:a[1])

# 정렬 기준이 되는 key를 순서대로 설정
# key1 : 국어 점수 내림 차순 정렬 >> 마이너스를 붙여서 정렬
# key2 : 영어 점수 오름 차순 정렬
# key3 : 수학 점수 내림 차순 정렬 >> 마이너스를 붙여서 정렬
# key4 : 이름을 사전순으로 정렬
score_list.sort(key=lambda a:((-a[1]), a[2], (-a[3]), a[0]))

print(score_list)

for i in score_list:
    print(i[0])