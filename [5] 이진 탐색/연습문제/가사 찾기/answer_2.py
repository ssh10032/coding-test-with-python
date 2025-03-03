import sys

sys.stdin = open("input.txt", "r")
def check_count(words, query):
    count = 0
    for word in words:
        if check_str(word, query):
            count+=1
        else:
            continue
    return count

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
    else:
        return False

def binary_search_start(words, query, start, end):
    result = -1
    while start <= end:
        mid = (start + end)//2
        if check_str(words[mid], query):
            result = mid
            end = mid-1
        else:
            if words[mid]>query:
                end = mid-1
            else:
                start = mid+1
    return result

def binary_search_end(words, query, start, end):
    result = -1
    while start <= end:
        mid = (start + end)//2
        if check_str(words[mid], query):
            result = mid
            start = mid+1
        else:
            if words[mid]>query:
                end = mid-1
            else:
                start = mid+1
    return result

# answer
# [3, 2, 4, 1, 0]
words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

words.sort()

print(words)

for query in queries:
    if query[0]!='?':
        print(query)
        start = binary_search_start(words, query, 0, len(words)-1)
        end = binary_search_end(words, query, 0, len(words)-1)
        if start == -1 and end==-1:
            print(0)
        else:
            print(end-start+1)
    else:
        print(query)
        print(check_count(words, query))