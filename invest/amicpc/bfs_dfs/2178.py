from pprint import pprint
from collections import deque
import copy

n, m = map(int, input().split())

maze = [[0 for i in range(m + 2)]]
for i in range(n):
    line = [0]
    tmp = input()
    for j in range(m):
        line.append(int(tmp[j]))
    line.append(0)
    maze.append(line)
maze.append([0 for i in range(m + 2)])

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

visited = [[1 for i in range(m + 2)]]
for i in range(n):
    line = [1] + [0 for _ in range(m)] + [1]
    visited.append(line)
visited.append([1 for i in range(m + 2)])

dist = [[1 for i in range(m + 2)]]
for i in range(n):
    line = [1] + [0 for _ in range(m)] + [1]
    dist.append(line)
dist.append([1 for i in range(m + 2)])

queue = deque()
queue.append((1, 1))
dist[1][1] = 1
visited[1][1] = 1

while queue:
    x, y = queue.popleft()
    for ax, ay in zip(dx, dy):
        nx, ny = x + ax, y + ay
        if visited[nx][ny] == 0 and maze[nx][ny]:
            queue.append((nx, ny))
            dist[nx][ny] = dist[x][y] + 1
            visited[nx][ny] = 1

# bfs는 현재 위치가 최단 경로라는 것을 보장할 수 있어서, 단순히 dist[nx][ny] =  dist[x][y]+1 이 가능하다
print(dist[n][m])
