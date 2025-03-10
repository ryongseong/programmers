from collections import deque

def solution(board):
    N = len(board) - 1 # index 0 is start 
    board_list = []
    answer = 0 # move_count

    for i in board:
        board_list.append(i)

    can, cant = 0, 1
    can_dia, cant_dia = 0, 1
    
    robot = deque()
    robot.append([0, 1, 0])

    def go_right(r, c):
        if board_list[r+1][c] is not cant:
            r, c += 1
            return r, c
    
    def go_left(r, c):
        if board_list[r-1][c] is not cant:
            r

    while robot:
        r, c, l = robot.popleft()




        if (r == N and l == N) or (c == N and l == N):
            break

    
    return answer

print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))