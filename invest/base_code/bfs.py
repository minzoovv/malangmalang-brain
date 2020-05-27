from collections import deque  # deque를 이용하면 popleft가 O(1)이다


def bfs(graph, visited, start):
    queue = deque()
    path = []
    # 초기화 작업
    queue.append(start)
    visited[start] = 1
    while queue:
        node = queue.popleft()
        path.append(node)
        # 여기에서 보통 다른 작업을 해준다. 그래프가 2차원 배열일 경우, dx와 dy를 두어 갈 수 있는 node에 대한 체크를 전부 해주는 등의 실행을 한다.
        for nx in graph[node]:
            if visited[nx] == 0:
                queue.append(nx)
                visited[nx] = 1
    return path


def solution(start):
    graph = {
        0: [1, 2],
        1: [2],
        2: [0, 1, 3],
        3: [2]
    }
    # 보통 graph는 2차원 배열일 수 있고, linked list와 같은 형태의 dict로 구현할 수도 있다.
    visited = [0 for _ in range(len(graph))]
    # visited의 구조는 문제에 따라서 달라질 수도 있다.

    path = bfs(graph, visited, start)
    return path


if __name__ == '__main__':
    print(solution(1))
