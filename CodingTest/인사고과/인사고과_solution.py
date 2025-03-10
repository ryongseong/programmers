def solution(scores):
    wanho = scores[0] # 완호의 점수는 0번째 인덱스에 있는 값들임
    wanho_sum = sum(wanho)
    scores.sort(key=lambda s: (-s[0], s[1])) # 0번 인덱스를 기준으로 내림차순, 1번 인덱스를 기준으로 오름차순을 함.
    max_company = 0 # 가장 높은 점수는 0으로 초깃값 할당
    answer = 1 # 등수는 1부터 시작하므로 1로 초깃값 할당
    for s in scores:
        if wanho[0] < s[0] and wanho[1] < s[1]: # 근무 태도와 동료 평가 둘 다 비교함. 한번이라도 두 점수 모두 낮은 경우가 한번이라도 있다면 
            return -1                           # 바로 return -1을 함.
        if max_company <= s[1]:                 # 0번 인덱스를 기준으로 내림차순을 했기 때문에 1번 인덱스를 비교함. 1번 인덱스의 값이 그 이전 사원이 1번 인덱스보다 작다면 조건 1에 만족을 하지 않으므로 패스함.
            if wanho_sum < s[0] + s[1]:         # 인센티브를 받을 수 있으므로 이제 완호의 등수를 매김
                answer += 1                     # 완호보다 총합이 높다면 등수가 높으므로 완호의 등수는 1씩 내려감
            max_company = s[1]                  # 이제 1번 인덱스를 다시 선언해줌.
    return answer                               # 등수를 리턴함.

# print(solution([[2,2], [1, 4], [3,2], [3, 2], [2, 1]]))
print(solution([[4, 0], [2, 3], [4, 4], [2, 6]]))
# answer => 4