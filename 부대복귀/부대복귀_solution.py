from collections import deque

def solution(n, roads, sources, destination):
    answer = []                                     # 정답지의 기본 설정 빈 리스트
    m = dict()                                      # m이라는 빈 딕셔너리 생성
    for i in range(1, n+1):                         # 1번부터 라고 했기에 1부터 만듦
        m[i] = list()                               # 1번부터 n까지의 key에 빈 리스트 생성

    for x,y in roads:                               # 경로
        m[x].append(y)                              # value로 경로 입력
        m[y].append(x)

    d = [-1] * (n + 1)                              # 거리 초깃값 -1로 생성
    q = deque()                                     # 빈 덱 생성
    q.append(destination)                           # 덱에 도착지 추가
    d[destination] = 0                              # 그 도착지는 움직일 필요가 없기에 시간 0

    while q:                                        # 덱이 빌 때까지
        x = q.popleft()                             # 덱에 있는 값중 왼쪽 값 빼서 x에 할당

        for y in m[x]:                              # 경로 탐색
            if d[y] == -1 or d[x] + 1 < d[y]:       # 뒤에꺼는 최단 시간을 위해 비교
                d[y] = d[x] + 1                     # 경로 이동 후 값 할당
                q.append(y)                         # 덱에 다음 이동 경로 추가

    for s in sources:                               # 서로 다른 지역 중 
        answer.append(d[s])                         # 그 값들만 정답지에 추가
        
    return answer                                   # 정답지 return

print(solution(3, [[1, 2], [2, 3]], [2, 3], 1))
# print(solution(5, [[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]], [1, 3, 5], 5))