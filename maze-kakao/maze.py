# https://school.programmers.co.kr/learn/courses/30/lessons/81304?language=python3

def solution(n, start, end, roads, traps):

    now = start
    answer = 0

    while now != end:
        for i in range(len(roads)):
            if now in traps:
                for j in range(len(roads)):
                    if now == roads[j][0] or now == roads[j][1]:
                        roads[j][0], roads[j][1] = roads[j][1], roads[j][0]
                    else:
                        continue

            if now == roads[i][0]:
                now = roads[i][1]
                answer += roads[i][2]

    return answer


# print(solution(3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2]))
print(solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3]))