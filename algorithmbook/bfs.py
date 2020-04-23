import queue  # queue와 deqeue 와 같은 built-in 자료구조를 잘 사용하자!


# using queue
def bfs(g, start):
    visited = {key: 0 for key in g.keys()}
    enqueued = {key: 0 for key in g.keys()}

    nodes = []
    q = queue.Queue()
    q.put(start)
    enqueued[start] = 1

    while not q.empty():
        node = q.get()
        for adjacent in g.get(node):
            if visited[adjacent] == 0 and enqueued[adjacent] == 0:
                q.put(adjacent)
                enqueued[adjacent] = 1
        visited[node] = 1
        nodes.append(node)
    return nodes


def bfs_paths(g, start, end):
    q = queue.Queue()
    q.put((start, [start]))

    while not q.empty():
        node, path = q.get()
        # set can do subtraction
        for neighbor in g[node] - set(path):
            if neighbor == end:
                yield path + [neighbor]
            else:
                q.put((neighbor, path + [neighbor]))


if __name__ == "__main__":
    graph = {
        'A': {'B', 'C'},
        'B': {'A', 'D', 'E'},
        'C': {'A', 'F'},
        'D': {'B'},
        'E': {'B', 'F'},
        'F': {'C', 'E'}
    }

    result = bfs(graph, 'A')
    path = list(bfs_paths(graph, 'A', 'F'))
    print(result, path)

