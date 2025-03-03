from bisect import bisect_left, bisect_right

# 나한테 부족했던 점
# ?가 포함된 문자열 탐색을 할때:
# >> 앞 문자열에 ? 가 포함되어 있을 때,
# 이진 탐색 못할거라고 생각하고, 완전 탐색으로 구현함.
# 근데 이진 탐색으로 만들 수 있음. 이진 탐색 문제면
# 예외 없이 다 이진 탐색으로 구현할 수 있다고 생각하고 접근해야함

# 1. 앞 문자열에 ?가 포함된 경우 : words, query 문자열 모두 뒤집어서 탐색
# 2. 뒤 문자열에 ?가 포함된 경우 : ?를 가장 앞과 뒤 알파벳 a, z로 치완해서 탐색
def count_by_range(arr, left_value, right_value):
    left_index = bisect_left(arr, left_value)
    right_index = bisect_right(arr, right_value)
    return right_index - left_index

def solution(words, queries):
    answer = []

    words_by_length = {}
    reversed_words_by_length = {}

    for word in words:
        length = len(word)
        words_by_length.setdefault(length, []).append(word)
        reversed_words_by_length.setdefault(length, []).append(word[::-1])

    for length in words_by_length:
        words_by_length[length].sort()
        reversed_words_by_length[length].sort()

    for query in queries:
        length = len(query)

        if length not in words_by_length:
            answer.append(0)
            continue

        if query[0] != '?':
            left_query = query.replace('?', 'a')
            right_query = query.replace('?', 'z')
            result = count_by_range(words_by_length[length], left_query, right_query)
        else:
            reversed_query = query[::-1]
            left_query = reversed_query.replace('?', 'a')
            right_query = reversed_query.replace('?', 'z')
            result = count_by_range(reversed_words_by_length[length], left_query, right_query)

        answer.append(result)
    return answer

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

print(solution(words, queries))