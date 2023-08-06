def solution(scores):
    answer = 1
    tops = {}
    up_list = []

    wanho_score = scores[0][0] + scores[0][1]
    for i in range(1, len(scores)):
        if scores[0][0] < scores[i][0] and scores[0][1] < scores[i][1]:
            return -1
        elif wanho_score < scores[i][0] + scores[i][1]:
            up_list.append([scores[i][0], scores[i][1]])
            if scores[i][0] not in tops:
                tops[scores[i][0]] = 0
            if tops[scores[i][0]] < scores[i][1]:
                tops[scores[i][0]] = scores[i][1]

    for i in range(len(up_list)):
        add = 1
        for k in tops:
            if k > up_list[i][0] and tops[k] > up_list[i][1]:
                add = 0
                break
        answer += add

    return answer
    
print(solution([[2,2], [1, 4], [3,2], [3, 2], [2, 1]]))