from collections import deque

def solution(n, roads, sources, destination):
    answer = []
    graph = [[] for _ in range(n + 1)]          # 각 지역이 1부터 시작하기에 n+1만큼 만들어 n개의 빈 리스트를 생성
    costs = [-1 for _ in range(n + 1)]          # 복귀가 불가능하면 -1이기에 -1로 초깃값 설정
    costs[destination] = 0                      # 도착지일 경우 움직일 필요가 없기에 0으로 설정
    queue = deque([destination])                # 큐에 도착지를 입력
    for n1, n2 in roads :                       # 왕복이 가능하기에 각각의 정보를 추가한다.
        graph[n1].append(n2)
        graph[n2].append(n1)
    while queue :                               # 큐가 빌때까지
        x = queue.popleft()                     # x에 queue 제일 왼쪽을 뺴서 넣음
        for node in graph[x] :                  # 갈 수 있는 경로를 탐색
            if costs[node] == -1 :
                queue.append(node)              # 갈 수 있는 경로를 큐에 추가 
                costs[node] = costs[x] + 1      # 그 경로로 이동, 두 지역 간의 길을 통과하는데 걸리는 시간이 모두 1로 동일하다고 했으므로 1을 추가해서 입력해줌.
    
    for s in sources :                          # 위의 코드가 끝나면 답안지를 작성
        answer.append(costs[s])                 # 그 경로로 가는데 걸리는 시간을 답안지에 추가.
    return answer