import sys

sys.stdin = open("input.txt", "r")

n = int(input())

stages = list(map(int, input().split()))

def solution(N, stages):
    fail_rates = []
    total_players = len(stages)

    for stage in range(1, N+1):
        # 현재 스테이지에 머물러 있는 사용자 수
        not_cleared = stages.count(stage)

        # 실패율 계산 (스테이지에 도달한 유저가 없는 경우 실패율 0)
        fail_rate = not_cleared/ total_players if total_players > 0 else 0

        # 실패율 리스트에 추가
        fail_rates.append((stage, fail_rate))

        # 현재 스테이지를 클리어하지 못한 사람 제외
        total_players -= not_cleared
    fail_rates.sort(key=lambda x:(-x[1], x[0]))

    return [stage for stage, _ in fail_rates]


print(solution(n, stages))