from collections import deque

def solution(food_times, k):

    food_list = deque()

    for index, food_time in enumerate(food_times):
        food_list.append([index, food_time])
    
    total_time = sum(food_times)

    if total_time <= k:
        return -1

    while food_list:
        food = food_list.popleft()
        
        food[1] -= 1
        if food[1] != 0:
            food_list.append(food)
        k -= 1
        if k == 0:
            break


    answer = food_list[0][0] + 1
    return answer


print(solution([3, 1, 2], 5))