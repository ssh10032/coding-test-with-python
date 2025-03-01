import sys

sys.stdin = open("input.txt", "r")

def check_str(word, query):
    if len(word)==len(query):
        for i in range(len(word)):
            if query[i]=='?':
                continue
            else:
                if word[i]==query[i]:
                    continue
                else:
                    return False
    return True
    # else:
    #     return False
def binary_search_right(words, query, start, end):
    result = -1
    while start <= end:
        mid = (start+end)//2
        if check_str(words[mid], query):
            result = mid
            start = mid+1
        else:
            if words[mid]>query:
                start = mid+1
            else:
                end = mid-1
    return result

def binary_search_left(words, query, start, end):
    result = -1
    while start <= end:
        mid = (start+end)//2
        if check_str(words[mid], query):
            result = mid
            end = mid-1
        else:
            if words[mid]>query:
                start = mid+1
            else:
                end = mid-1
    return result
# def binary_search_str()

# answer : [3, 2, 4, 1, 0]
words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

# 이진 탐색???
words.sort()

words_len = len(words)
print(words)

print(check_str(words[1], queries[0]))
print(binary_search_left(words, queries[0], 0, words_len-1))
print(binary_search_right(words, queries[0], 0, words_len-1))
#
print(words[0]>queries[2])

# for i in queries:
#     min_idx = binary_search_left(words, i, 0, words_len-1)
#     max_idx = binary_search_right(words, i, 0, words_len-1)
#     print(i)
#     print(min_idx)
#     print(max_idx)
#     print(max_idx-min_idx+1)
#     print(' ')