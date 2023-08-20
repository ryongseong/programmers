def solution(food_times, k):
    food_list = []

    for idx, food_time in enumerate(food_times):
        food_list.append([idx, food_time])

    if sum(food_times) <= k:
        return -1
    else:
        while k != 0:
            food = food_list.pop(0)
            food[1] -= 1
            if food[1] != 0:
                food_list.append(food)
            k -= 1
    answer = food_list[0][0] + 1
    return answer

print(solution([3, 1, 2], 5))