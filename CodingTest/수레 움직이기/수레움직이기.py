from collections import deque
from copy import deepcopy


def solution(maze):
    n, m = len(maze), len(maze[0])

    queue = deque()
    red_visited, blue_visited = [[0] * 4 for _ in range(4)], [[0] * 4 for _ in range(4)]
    directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]
    red_start, blue_start = [], []

    for r in range(n):
        for c in range(m):
            cur = maze[r][c]
            if cur == 1:
                red_start = [r, c, 0]
                red_visited[r][c] = 1
            elif cur == 2:
                blue_start = [r, c, 0]
                blue_visited[r][c] = 1

    queue.append([red_start, blue_start, red_visited, blue_visited])

    while queue:
        red_cur, blue_cur, r_visited, b_visited = queue.popleft()

        rr, rc, rt = red_cur
        br, bc, bt = blue_cur

        if maze[rr][rc] == 3 and maze[br][bc] == 4:
            return rt if rt > bt else bt

        if maze[rr][rc] == 3:
            for dr, dc in directions:
                bnr, bnc = br + dr, bc + dc
                if canMove(bnr, bnc, b_visited, maze, n, m):
                    if not (bnr == rr and bnc == rc):
                        b_visited[bnr][bnc] = 1
                        queue.append(
                            [[rr, rc, rt + 1], [bnr, bnc, bt + 1], r_visited, b_visited]
                        )
        elif maze[br][bc] == 4:
            for dr, dc in directions:
                rnr, rnc = rr + dr, rc + dc
                if canMove(rnr, rnc, r_visited, maze, n, m):
                    if not (rnr == br and rnc == bc):
                        r_visited[rnr][rnc] = 1
                        queue.append(
                            [[rnr, rnc, rt + 1], [br, bc, bt + 1], r_visited, b_visited]
                        )
        else:
            for dr, dc in directions:
                rnr, rnc = rr + dr, rc + dc
                r_copy_visited = deepcopy(r_visited)
                b_copy_visited = deepcopy(b_visited)

                if not canMove(rnr, rnc, r_copy_visited, maze, n, m):
                    continue

                for dr, dc in directions:
                    bnr, bnc = br + dr, bc + dc
                    if canMove(bnr, bnc, b_copy_visited, maze, n, m):
                        if not (rnr == bnr and rnc == bnc) and not (
                            rnr == br and rnc == bc and bnr == rr and bnc == rc
                        ):
                            r_copy_visited[rnr][rnc] = 1
                            b_copy_visited[bnr][bnc] = 1
                            queue.append(
                                [
                                    [rnr, rnc, rt + 1],
                                    [bnr, bnc, bt + 1],
                                    r_copy_visited,
                                    b_copy_visited,
                                ]
                            )

    return 0


def canMove(r, c, visited, maze, n, m):
    if 0 <= r < n and 0 <= c < m and maze[r][c] != 5 and not visited[r][c]:
        return True
    return False
