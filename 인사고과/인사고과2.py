def solution(scores):
    wanho = scores[0] # 완호의 점수는 0번째 인덱스에 있는 값들임
    wanho_sum = sum(wanho)
    scores.sort(key=lambda s: (-s[0], s[1])) # 0번 인덱스를 기준으로 내림차순, 1번 인덱스를 기준으로 오름차순을 함.
    max_company = 0 # 가장 높은 점수는 0으로 초깃값 할당
    answer = 1 # 등수는 1부터 시작하므로 1로 초깃값 할당
    for s in scores:
        if wanho[0] < s[0] and wanho[1] < s[1]: # 근무 태도와 동료 평가 둘 다 비교함. 한번이라도 두 점수 모두 낮은 경우가 한번이라도 있다면 바로 return -1을 함.
            return -1
        if max_company <= s[1]: # 
            if wanho_sum < s[0] + s[1]:
                answer += 1
            max_company = s[1]
    return answer

print(solution([[2,2], [1, 4], [3,2], [3, 2], [2, 1]]))
# answer => 4