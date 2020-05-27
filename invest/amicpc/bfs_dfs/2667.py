# 단지번호 붚이기

from collections import deque
from pprint import pprint

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(danji, visited, x, y):
    han_danji = []
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()
        han_danji.append((x, y))

        for i in range(len(dx)):
            nx, ny = x + dx[i], y + dy[i]
            if (-1 < nx < n and -1 < ny < n) and danji[nx][ny] == 1 and visited[nx][ny] == 0:
                queue.append((nx, ny))
                visited[nx][ny] = 1

    print(han_danji)
    return han_danji


n = int(input())

danji = [[int(i) for i in input()] for _ in range(n)]
visited = [[0] * n for _ in range(n)]

num_danji = []
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0 and danji[i][j] == 1:
            num_danji.append(len(bfs(danji, visited, i, j)))
            # 처음에 string으로 바꾸고 sorting 해주니, 이상한 결과가 나왔다

print(len(num_danji))
for num in sorted(num_danji):
    print(num)
