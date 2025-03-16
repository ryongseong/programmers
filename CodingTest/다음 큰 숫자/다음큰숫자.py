def solution(n):
    answer = n + 1

    while True:
        if bin(answer)[2:].count("1") == bin(n)[2:].count("1"):
            break
        answer += 1
    return answer


print(solution(78))  # 83
print(solution(15))  # 23
