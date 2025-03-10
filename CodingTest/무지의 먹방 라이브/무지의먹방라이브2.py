from collections import deque

def solution(food_times, k):
    answer = -1

    queue = deque()

    for idx, food_time in enumerate(food_times):
        queue.append([idx+1, food_time])
    
    while queue:
        if k != 0:
            food = queue.popleft()
            
            if food[1] == 0:
                pass
            else:
                food[1] -= 1
                queue.append(food)
                k -= 1
        else:
            answer = queue[0][0]
            break
        
    return answer

print(solution([3, 1, 2], 5))