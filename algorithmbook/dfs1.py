from sys import stdin
read = lambda: stdin.readline().split()

# 그대로 따라했는데 왜 오답으로 나오는지 모르겠따ㅠ
UNWATCHED, WATCHED, INSTALLED = 0, 1, 2


def dfs(gallery, edges):
    global camera
    visited[gallery] = 1
    neighbors = edges.get(gallery, [])
    children = [0, 0, 0]  # represent the state of child node
    for neighbor in neighbors:
        if not visited[neighbor]:
            children[dfs(neighbor, edges)] += 1

    if children[UNWATCHED]:
        camera += 1
        return INSTALLED

    if children[INSTALLED]:
        return WATCHED

    return UNWATCHED


N = int(input())

for _ in range(N):
    G, H = map(int, read())
    edges = {}
    for _ in range(H):
        g1, g2 = map(int, read())
        if g1 not in edges.keys():
            edges[g1] = [g2]
        else:
            edges[g1].append(g2)

    camera = 0
    visited = [0 for _ in range(G)]
    for g in range(G):
        if not visited[g] and dfs(g, edges) == UNWATCHED:
            camera += 1
    print(camera)

