from sys import stdin, stdout
read = lambda: stdin.readline().split()

blocks = [
    ((0, 0), (0, -1), (1, 0)),
    ((0, 0), (-1, 0), (1, 0)),
    ((0, 0), (0, -1), (1, 0)),
    ((0, 0), (0, -1), (1, 0))
]

def cover(board, H, W):
    check_case = []
    init = 0
    is_black = 1
    space_counter = 0
    # check all board is covered
    for line in board:
        space_counter += line.count('.')
        if line.count('.') > 0:
            is_black = 0

    if is_black:
        return 1
    if space_counter % 3:
        return init

    else:
        # make check case
        for i in range(H):
            for j in range(W):
                if board[i][j] == '.':
                    if i > 0 and j > 0:
                        if board[i][j-1] == board[i-1][j] == '.':
                            board[i][j-1] == board[i-1][j]
                    if i < W and j > 0:
                        check_case.append([board[i][j-1], board[i+1][j]])
                    if i > 0 and j < H:
                        check_case.append([board[i-1][j], board[i][j+1]])
                    if i < W and j < H:
                        check_case.append([board[i][j-1], board[i-1][j]])

                else:
                    pass


    return init

C = int(input())

for _ in range(C):
    H, W = map(int, read())
    board = [list(map(str, read())) for _ in range(H)]
    result = cover(board, H, W)





