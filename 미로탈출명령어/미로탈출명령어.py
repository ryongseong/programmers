from collections import deque


def solution(n, m, x, y, r, c, k):
    directions = [(1, 0, "d"), (0, -1, "l"), (0, 1, "r"), (-1, 0, "u")]

    min_moves = abs(r - x) + abs(c - y)

    if min_moves > k or (k - min_moves) % 2 != 0:
        return "impossible"

    queue = deque([(x - 1, y - 1, "", 0)])
    visited = set()

    while queue:
        cr, cc, path, cnt = queue.popleft()

        if cnt == k:
            if (cr, cc) == (r - 1, c - 1):
                return path
            continue

        for dr, dc, d in directions:
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < n and 0 <= nc < m and (nr, nc, cnt + 1) not in visited:
                visited.add((nr, nc, cnt + 1))
                queue.append((nr, nc, path + d, cnt + 1))

    return "impossible"
