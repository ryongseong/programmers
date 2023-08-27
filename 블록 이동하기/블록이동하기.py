def solution(board):
    board_list = []

    for i in board:
        board_list.append(i)

    robot = board_list[0][0:2]

    answer = 0
    return answer

print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))