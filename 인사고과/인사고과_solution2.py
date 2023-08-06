def solution(scores):
    s1, s2 = scores[0]                          # 완호의 점수를 언패킹하여 s1, s2에 할당.
    scores.sort(key=lambda x: (-x[0], x[1]))    # 점수를 0번 인덱스를 기준으로 내림차순, 1번 인덱스를 기준으로 오름차순한다. 

    rank, bar = 1, 0                            # 등수와 점수의 기준을 1과 0으로 초깃값 할당.
    for x, y in scores:                         # scores에 들어있는 값들을 하나씩 언패킹하여 x, y에 할당.
        if s1+s2 < x+y and bar <= y:            # 완호의 점수가 x+y보다 작으면서, 기준점이 y보다 작거나 같다면
            rank += 1                           # 등수가 한 단계 내려감.

        if s1 == x and s2 == y and bar > y:     # 완호의 근무 태도 점수가 x와 같고, 동료 평가 점수가 y와 같으면서 기준점이 y보다 크다면 완호보다 점수가 낮은 사람이 없다는 말이므로,
            return -1                           # 성과급여를 못받기에 -1을 리턴한다.

        bar = max(bar, y)                       # 기준점을 다시 할당해준다.

    return rank                                 # 등수를 반환한다.

# print(solution([[2,2], [1, 4], [3,2], [3, 2], [2, 1]]))
print(solution([[7, 1], [6, 6], [5, 4], [5, 4], [6, 6]]))