def solution(mats, park):
    answer = -1

    rows = len(park)
    cols = len(park[0])
    mats.sort()

    for i in range(len(mats) -1, -1, -1):
        flag = False

        for j in range(rows - mats[i] + 1):
            for l in range(cols - mats[i] + 1):
                flag2 = True

                for k in range(j, j + mats[i]):
                    for x in range(l, l + mats[i]):
                        if park[k][x] != '-1': flag2 = False; break
                
                    if not flag2: break

                if flag2:
                    flag = True
                    break
            
            if flag:
                break
        
        if flag:
            answer = mats[i]
            break

    return answer

print(solution(mats=[5, 3, 2], park=[["A", "A", "-1", "B", "B", "B", "B", "-1"], ["A", "A", "-1", "B", "B", "B", "B", "-1"], ["-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1"], ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"], ["D", "D", "-1", "-1", "-1", "-1", "-1", "F"], ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"]]))
# 3