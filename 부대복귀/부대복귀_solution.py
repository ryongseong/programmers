from collections import deque

def solution(n, roads, sources, destination):
    answer = []
    m = dict()
    for i in range(1, n+1):
        m[i] = list()

    for x,y in roads:
        m[x].append(y)
        m[y].append(x)

    d = [-1] * (n + 1)
    q = deque()
    q.append(destination)
    d[destination] = 0

    while q:
        x = q.popleft()

        for y in m[x]:
            if d[y] == -1 or d[x] + 1 < d[y]:
                d[y] = d[x] + 1
                q.append(y)

    for s in sources:
        answer.append(d[s])
        
    return answer

print(solution(3, [[1, 2], [2, 3]], [2, 3], 1))
# print(solution(5, [[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]], [1, 3, 5], 5))