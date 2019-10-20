def rotate_key(key):
    temp_matrix = [[0 for _ in range(len(key))] for _ in range(len(key))]
    for j in range(len(key)):
        counter = 0
        for i in range(len(key)):
            temp_matrix[counter][len(key)-j-1] = key[j][i]
            counter += 1
    return temp_matrix


def add_key_to_board(board, key, start_point):
    new_board = [[i for i in j] for j in board]
    for k in range(len(key)):
        for v in range(len(key)):
            new_board[start_point[0]+k][start_point[1]+v] += key[k][v]
    return new_board


def check_enable_unlock(key, lock):
    for i in range(4):
        len_board = len(key) * 2 + len(lock) - 2
        # make board
        board = [[0 for _ in range(len_board)] for _ in range(len_board)]

        # set a lock on the board
        for i_a in range(len(key)-1, (len(key)-1)+len(lock)):
            for j_a in range(len(key)-1, (len(key)-1)+len(lock)):
                board[i_a][j_a] = lock[i_a-(len(key)-1)][j_a-(len(key)-1)]

        # check the board area
        for i_b in range(len_board-(len(key)-1)):
            for j_b in range(len_board-(len(key)-1)):
                result_board = add_key_to_board(board, key, (i_b, j_b))
                result = True
                for k in range(len(key)-1, (len(key)-1) + len(lock)):
                    for v in range(len(key)-1, (len(key)-1) + len(lock)):
                        if result_board[k][v] != 1:
                            result = False
                if result:
                    return True

        # rotate key
        key = rotate_key(key)
    return False


def solution(key, lock):
    answer = check_enable_unlock(key, lock)
    return answer

