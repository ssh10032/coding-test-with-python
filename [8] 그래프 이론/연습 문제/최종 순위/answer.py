import sys

sys.stdin = open("input.txt", "r")

# 대회 예선에 총 n개의 팀 참여
# 팀은 1번부터 n번까지 번호 매겨짐
# 작년에 비해서 상대적 순위가 바뀐 팀의 목록만 발표
# 작년에는 순위를 발표함
# 예를 들어 작년에 팀 13이 팀 6보다 순위가 높았는데,
# 올해 팀 6이 팀13보다 순위가 높으면 (6, 13)을 발표

# 작년 순위와 상대적 순위가 바뀐 모든 팀의 목록이 주어지면
# 올해 순위를 만드는 프로그램 작성

# 하지만
#1 확실한 올해 순위를 만들어 낼 수 없는 경우도 있음
#2 일관성이 없는 잘못된 정보일 수도 있음

# 첫째 줄은 테스트 케이스의 수
test = int(sys.stdin.readline().rstrip())

for _ in range(test):
    # 팀 수 n
    n = int(sys.stdin.readline().rstrip())
    # 작년 팀 성적 순위
    p_rank = list(map(int, sys.stdin.readline().rstrip().split()))
    # 상대적인 등수가 바뀐 쌍의 수
    m = int(sys.stdin.readline().rstrip())
    # 바뀐 팀 쌍들
    c_rank = []
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        c_rank.append((a,b))
    print(p_rank)
    print(c_rank)