from bisect import bisect_left, bisect_right

def count_by_range(arr, left_value, right_value):
    left_index = bisect_left(arr, left_value)
    right_index = bisect_right(arr, right_value)
    return right_index-left_index

def answer(words, queries):

    answer = []
    words_by_length = {}
    reversed_words_by_length = {}

    for word in words:
        length = len(word)

        words_by_length.setdefault(length, []).append(word)
        reversed_words_by_length.setdefault(length, []).append(word[::-1])

    # 이진 탐색 하기 전에 정렬했는지 반드시 점검!!
    for length in words_by_length:
        words_by_length[length].sort()
        reversed_words_by_length[length].sort()

    for query in queries:
        length = len(query)

        if length not in words_by_length:
            answer.append(0)
        else:
            if query[0]!='?':
                left_value = query.replace('?', 'a')
                right_value = query.replace('?', 'z')
                query_count = count_by_range(words_by_length[length], left_value, right_value)

            else:
                reversed_query = query[::-1]
                left_value = reversed_query.replace('?', 'a')
                right_value = reversed_query.replace('?', 'z')
                query_count = count_by_range(reversed_words_by_length[length], left_value, right_value)
            answer.append(query_count)
    return answer




# words_by_length.setdefault(length, []).append(word)


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

print(answer(words, queries))