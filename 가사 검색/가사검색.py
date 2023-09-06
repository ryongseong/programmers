def solution(words, queries):
    answer = []

    query_list = []
    for query in queries:
        len_query = len(query)
        q = query.strip("?")
        query_list.append([len_query, q])

    while query_list:
        length, compare = query_list.pop(0)
        


    return answer


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))

# result
# [3, 2, 4, 1, 0]