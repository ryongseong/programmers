def solution(food_times, k):
    food_list = []
    totalTime = 0

    for i in range(len(food_times)):
        food_list.append([i, food_times[i]])
        totalTime += food_times[i]

    if totalTime <= k:
        return -1

    food_list = sorted(food_list, key = lambda x:x[1])

    delTime = food_list[0][1]*len(food_list)
    i = 1
    
    while delTime < k:
        k -= delTime
        delTime = (food_list[i][1] - food_list[i-1][1]) * (len(food_list) - i)
        i += 1

    food_list = sorted(food_list[i-1:], key = lambda x:x[0])
    
    return food_list[k%len(food_list)][0]+1

print(solution([3, 1, 2], 5))
