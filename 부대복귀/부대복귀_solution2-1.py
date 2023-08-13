import heapq

def solution(n, roads, sources, destination):
    graph = [[] for _ in range(n + 1)]                  
    inf = float("inf")                                  
    cost = [inf for _ in range(n + 1)]                  
    answer = []

    for road in roads:                                  
        graph[road[0]].append(road[1])                 
        graph[road[1]].append(road[0])

    h = [(0, destination)]                              
    cost[destination] = 0                               
    while h:                                            
        c, curr = heapq.heappop(h)                      
        if c <= cost[curr]:                             
            for g in graph[curr]:                       
                if c + 1 < cost[g]:                     
                    cost[g] = c + 1                     
                    heapq.heappush(h, (cost[g], g))     

    for idx in sources:
        if cost[idx] != inf:
            answer.append(cost[idx])
        else:
            answer.append(-1)

    return answer
    # return [cost[idx] if cost[idx] != inf else -1 for idx in sources]   # source안에 있는 정보 중에서 inf가 아닌 것은 출력하고 inf인 것은 -1로 출력

print(solution(3, [[1, 2], [2, 3]], [2, 3], 1))
# print(solution(5, [[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]], [1, 3, 5], 5))