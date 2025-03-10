def solution(food_times, k):
    food_list = []

    for i in range(len(food_times)):
        food_list.append([i, food_times[i]])

    # 시간의 합이 k초보다 작다면 k초 후에 먹을 음식이 없기에 -1을 반환
    if sum(food_times) <= k:
        return -1

    # 시간을 기준으로 오름차순
    food_list.sort(key= lambda x:x[1])

    # 바퀴를 돌 때 시간이 가장 작은 음식을 다 먹는데 걸리는 시간
    delTime = food_list[0][1]*len(food_list)

    # 음식 번호
    i = 1
    
    while delTime < k:
        k -= delTime
        delTime = (food_list[i][1] - food_list[i-1][1]) * (len(food_list) - i)
        i += 1

    food_list = sorted(food_list[i-1:], key = lambda x:x[0])
    
    return food_list[k%len(food_list)][0]+1

print(solution([3, 1, 2], 5))
