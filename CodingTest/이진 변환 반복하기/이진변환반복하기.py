def solution(s):
    cnt, zero_cnt = 0, 0

    while s != "1":
        cnt += 1
        num = s.count("1")
        zero_cnt += len(s) - num
        s = bin(num)[2:]

    return [cnt, zero_cnt]


print(solution("110010101001"))  # [3,8]
