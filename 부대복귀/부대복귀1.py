from collections import deque

def solution(n, roads, sources, destination):
    answer = []
    graph = [[] for _ in range(n + 1)]          # 각 지역이 1부터 시작하기에 n+1만큼 만들어 n개의 빈 리스트를 생성
    costs = [-1 for _ in range(n + 1)]          # 복귀가 불가능하면 -1이기에 -1로 초깃값 설정
    costs[destination] = 0
    queue = deque([destination])
    for n1, n2 in roads :                       # 왕복이 가능하기에 각각의 정보를 추가한다.
        graph[n1].append(n2)
        graph[n2].append(n1)
    while queue :
        x = queue.popleft()
        for node in graph[x] :
            if costs[node] == -1 :
                queue.append(node) 
                costs[node] = costs[x] + 1
    for s in sources :
        answer.append(costs[s])
    return answer