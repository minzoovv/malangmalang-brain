# 1에서 왔을 때, 2, 3을 1로 갱신
# 2, 3을 먼저 또 실행, 2 에서는 자신 +1 4 자신 +1 5 갱신
# 3에서는 자신 +1 과 2에 있는 수 갱신
# 이런식으로 했을때, 가장 최대 값을 가지는 수의 index return.
# 1은 0으로 생각하자.

# dijkstra로 하면 된다

from collections import deque, defaultdict
from math import inf


def djikstra(start, table, edge):
    queue = deque()
    queue.append(start)

    while queue:
        node = queue.popleft()
        for e in edge[node]:
            if table[e] == inf:
                table[e] = table[node] + 1
                queue.append(e)
            else:
                table[e] = min(table[e], table[node] + 1)


def solution(n, edge):
    table = [inf for _ in range(n + 1)]
    table[0] = 0
    table[1] = 0

    edge_map = defaultdict(list)
    for e in edge:
        edge_map[e[0]].append(e[1])
        edge_map[e[1]].append(e[0])

    djikstra(1, table, edge_map)

    return table.count(max(table))