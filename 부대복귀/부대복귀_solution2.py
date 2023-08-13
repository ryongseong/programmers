# 커밋 잘못한 이유로 다시 푸쉬
import heapq

def solution(n, roads, sources, destination):
    graph = [[] for _ in range(n + 1)]                  # 각 지역이 1부터 시작하기에 n+1만큼 만들어 n개의 빈 리스트를 생성
    inf = float("inf")                                  # inf라는 무한대 생성 
    cost = [inf for _ in range(n + 1)]                  # cost에 다 n+1개만큼 무한대로 리스트 생성

    for road in roads:                                  # 왕복이 가능하기에 각각의 정보 추가
        graph[road[0]].append(road[1])                 
        graph[road[1]].append(road[0])

    h = [(0, destination)]                              # 큐에 시간과 도착지 추가
    cost[destination] = 0                               # 도착지에서는 움직일 필요가 없기에 시간을 0으로 설정
    while h:                                            # 큐가 빌 때까지
        c, curr = heapq.heappop(h)                      # 현재 걸린 시간과 현재 위치를 c, curr에 할당
        if c <= cost[curr]:                             # 현재 걸린 시간이 그 위치의 시간보다 작거나 같아야 함.(문제 조건에서 최소의 시간을 구하라고 했기 때문)
            for g in graph[curr]:                       # 현재 위치에서 갈 수 있는 경로 탐색
                if c + 1 < cost[g]:                     # 갈 수 있는 곳 중 거리 비용이 더 작다면
                    cost[g] = c + 1                     # 현재 걸린 시간에 1을 추가하여 g의 거리값에 할당
                    heapq.heappush(h, (cost[g], g))     # 큐에 그 시간 정보와 다음 목적지 추가

    return [cost[idx] if cost[idx] != inf else -1 for idx in sources]   # source안에 있는 정보 중에서 inf가 아닌 것은 출력하고 inf인 것은 -1로 출력

print(solution(3, [[1, 2], [2, 3]], [2, 3], 1))
# print(solution(5, [[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]], [1, 3, 5], 5))