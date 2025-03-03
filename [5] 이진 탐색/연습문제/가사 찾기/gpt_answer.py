from bisect import bisect_left, bisect_right

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