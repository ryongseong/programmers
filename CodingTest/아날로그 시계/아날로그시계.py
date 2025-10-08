def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    start = h1 * 3600 + m1 * 60 + s1
    end = h2 * 3600 + m2 * 60 + s2

    if start == 0 or start == 43200:
        answer += 1

    for hour in range(start, end):
        c_hour_angle = hour / 120 % 360
        c_min_angle = hour / 10 % 360
        c_sec_angle = hour * 6 % 360

        n_hour_angle = (hour + 1) / 120 % 360
        n_min_angle = (hour + 1) / 10 % 360
        n_sec_angle = (hour + 1) * 6 % 360

        if n_hour_angle == 0:
            n_hour_angle = 360
        if n_min_angle == 0:
            n_min_angle = 360
        if n_sec_angle == 0:
            n_sec_angle = 360

        if c_sec_angle < c_hour_angle and n_sec_angle >= n_hour_angle:
            answer += 1
        if c_sec_angle < c_min_angle and n_sec_angle >= n_min_angle:
            answer += 1
        if n_hour_angle == n_sec_angle and n_min_angle == n_sec_angle:
            answer -= 1

    return answer


print(solution(0, 5, 30, 0, 7, 0))  # 2
print(solution(0, 0, 0, 23, 59, 59))  # 2852
print(solution(12, 0, 0, 12, 0, 30))  # 1
print(solution(11, 59, 30, 12, 0, 0))  # 1
