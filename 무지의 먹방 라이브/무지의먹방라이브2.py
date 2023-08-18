import heapq

def solution(food_times, k):
    answer = -1
    food_list = []
    for i in range(len(food_times)):
        heapq.heappush(food_list, (food_times[i], i+1))

    foods = len(food_times)
    p = 0

    while food_list:
        t = (food_list[0][0] - p) * foods
        
        if k >= t:
            k -= t
            p, index = heapq.heappop(food_list)
            foods -= 1
        else:
            idx = k % foods
            food_list.sort(key=lambda x : x[1])
            answer = food_list[idx][1]
            break

    return answer

print(solution([3, 1, 2], 5))