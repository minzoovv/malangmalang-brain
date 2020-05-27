# 토마토
import sys

n, m = map(int, input().split())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def ripe(tomatos, targets, n, m):
    new_target = []
    for target in targets:
        for i in range(len(dx)):
            nx, ny = target[0] + dx[i], target[1] + dy[i]
            if (0 <= nx < m and 0 <= ny < n) and tomatos[nx][ny] == 0:
                new_target.append((nx, ny))
                tomatos[nx][ny] = 1
                # 여기서 visited check를 해주어야 한다. queue에 들어가 있을 때 visited 처리 해준다

    return new_target


# def check_all_ripped(tomatos):
#     return not any(any(t == 0 for t in tomato) for tomato in tomatos)
# 이 부분이 시간이 굉장히 오래걸려서, 그냥 토마토 개수를 세어주는 형식으로 다 익었는지를 체크히였다.

tomatos = []
for _ in range(m):
    tomatos.append(list(map(int, sys.stdin.readline().split())))

targets = []
rotten = 0
count = 0
for i in range(m):
    for j in range(n):
        if tomatos[i][j] == 1:
            targets.append((i, j))
            count += 1
        elif tomatos[i][j] == -1:
            rotten += 1  # 썩은 토마토도 세어주었다

answer = 0

while targets and count <= m * n:
    targets = ripe(tomatos, targets, n, m)
    answer += 1
    count += len(targets)  # 다음에 들어오는 토마토들은 전부 익은 것

if count == m * n - rotten:
    print(answer - 1)
else:
    print(-1)
