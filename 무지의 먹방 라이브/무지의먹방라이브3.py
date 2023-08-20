from collections import deque
import sys
sys.setrecursionlimit(10**9)

def solution(food_times, k):
    
    food_list = deque()
    for idx, food in enumerate(food_times):
        food_list.append([idx, food])
    
    if sum(food_times) <= k:
        return -1
    else:
        sol(food_list, k)
    answer = food_list[0][0] + 1
    return answer

def sol(food_list, k):
    food = food_list.popleft()

    k -= 1
    food[1] -= 1

    if food[1] != 0:
        food_list.append(food)
    
    if k != 0:
        sol(food_list, k)

print(solution([3, 1, 2], 5))