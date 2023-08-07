def solution(scores):
    answer = 1

    wanho = scores.pop(0)
    wanho_sum = sum(wanho)

    scores.sort(key=lambda x: (-x[0], x[1])) 

    for a, b in scores:

        if wanho_sum < a + b:
            answer += 1
        
        if wanho[0] < a and wanho[1] < b:
            return -1
    
    return answer

print(solution([[7, 1], [6, 6], [5, 4], [5, 4], [6, 6]]))  # 출력: 3