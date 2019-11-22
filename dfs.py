

# using stack, visit all vertice
def dfs(g, start):
    visited = {key: 0 for key in graph.keys()}
    stk = [start]

    nodes = []
    while stk:
        node = stk.pop()
        for adjacent in g[node]:
            if visited[adjacent] == 0 and adjacent not in stk:
                stk.append(adjacent)
        visited[node] = 1
        nodes.append(node)
    return nodes


# get shortest path of dfs
def dfs_path(g, start, end):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for neighbor in graph[vertex] - set(path):
            if neighbor == end:
                yield path + [neighbor]
            else:
                stack.append((neighbor, path + [neighbor]))

if __name__ == "__main__":
    graph = {
        'A': {'B', 'C'},
        'B': {'A', 'D', 'E'},
        'C': {'A', 'F'},
        'D': {'B'},
        'E': {'B', 'F'},
        'F': {'C', 'E'}
    }

    result = dfs(graph, 'A')
    paths = list(dfs_path(graph, 'A', 'D'))
    print(result, paths)


