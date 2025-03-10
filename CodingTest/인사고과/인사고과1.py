def solution(scores):
    woanho_scores = scores[0][0] + scores[0][1]
    
    if all(woanho_scores >= score[0] + score[1] for score in scores):
        return -1

    ranks = 1
    for score in scores[1:]:
        total_score = score[0] + score[1]
        if woanho_scores < total_score:
            ranks += 1

    return ranks

# 테스트
print(solution([[2,2],[1,4],[3,2],[3,2],[2,1]]))  # 출력: 4
