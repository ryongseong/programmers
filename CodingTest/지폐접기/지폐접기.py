def solution(wallet, bill):
    answer = 0

    while True:
        if (wallet[0] >= bill[0] and wallet[1] >= bill[1]) or (wallet[0] >= bill[1] and wallet[1] >= bill[0]):
            break
        if bill[0] > bill[1]:
            bill[0] //= 2
            answer += 1
        else:
            bill[1] //= 2
            answer += 1

    return answer

# print(solution(wallet=[30, 15], bill=[26, 17])) # 1
print(solution(wallet=[50, 50], bill=[100, 241])) # 4