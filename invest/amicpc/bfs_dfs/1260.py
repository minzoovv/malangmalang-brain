import sys
import collections


def bfs(graph, start, n):
    path = []
    visited = [0 for _ in range(n + 1)]
    queue = collections.deque()
    queue.append(start)
    while queue:
        node = queue.popleft()
        if visited[node] != 0:
            continue
        visited[node] = 1
        path.append(node)
        for next in sorted(graph[node]):
            if visited[next] == 0:
                queue.append(next)

    return path


def dfs(graph, start, n):
    path = []
    visited = [0 for _ in range(n+1)]

    stack = collections.deque()
    stack.append(start)
    while stack:
        node = stack.pop()
        if visited[node] != 0:
            continue
        visited[node] = 1
        path.append(node)
        for next in sorted(graph[node], reverse=True):
            if visited[next] == 0:
                stack.append(next)

    return path


n, m, v = map(int, input().split())

graph = collections.defaultdict(set)
for _ in range(m):
    start, end = map(int, input().split())
    graph[start].add(end)
    graph[end].add(start)

print(' '.join(map(str, dfs(graph, v, n))))
print(' '.join(map(str, bfs(graph, v, n))))

# set은 정렬을 보장해주지 않는다. 넣고 빼는 순서대로 정렬해줄 뿐.