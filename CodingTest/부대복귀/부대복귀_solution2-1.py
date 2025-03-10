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
