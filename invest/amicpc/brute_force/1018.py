from sys import stdin

n, m = map(int, stdin.readline().split(" "))

board = []
for _ in range(n):
    line = str(input())
    board.append(line)

answer = 64

for i in range(n-7):
    for j in range(m-7):
        count_for_start_b = 0  # 왼쪽 첫째칸이 검은색일 때 바꿔야 할 것의 개수
        count_for_start_w = 0  # 왼쪽 첫째칸이 흰색일 때 바꿔야 할 것의 개수
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l) % 2 == 0:  # 왼쪽 첫째칸의 색과 동일해야 한다.
                    if board[k][l] == 'B':
                        count_for_start_w += 1 # 왼쪽 첫째칸이 흰색인데, 현재 검은색이므로 바꿔야한다.
                    else:
                        count_for_start_b += 1 # 왼쪽 첫째칸이 검은색인데, 현재 흰색이므로 바꿔야한다.
                else:  # 왼쪽 첫째칸 색과 달라야 한다.
                    if board[k][l] == 'B':
                        count_for_start_b += 1 # 왼쪽 첫째칸이 검은색인데, 현재 검은색이므로 바꿔야 한다.
                    else:
                        count_for_start_w += 1 # 왼쪽 첫째칸이 흰색인데, 흰색이므로 바꾸어야 한다.
        print(count_for_start_w, count_for_start_b)
        answer = min(answer, count_for_start_b, count_for_start_w)

print(answer)



