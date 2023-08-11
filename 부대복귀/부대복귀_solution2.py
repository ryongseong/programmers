# 커밋 잘못한 이유로 다시 푸쉬
import heapq

def solution(n, roads, sources, destination):
    graph = [[] for _ in range(n + 1)]
    cost = [int(1e5) for _ in range(n + 1)]

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

    return [cost[idx] if cost[idx] != int(1e5) else -1 for idx in sources]

print(solution(3, [[1, 2], [2, 3]], [2, 3], 1))
# print(solution(5, [[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]], [1, 3, 5], 5))