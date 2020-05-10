def bfs(link, start, dest):
    queue = []
    visited = []
    dist = {}

    dist[start] = 0
    queue.append(start)
    while queue:
        target = queue.pop(0)
        if target in visited:
            continue
        visited.append(target)

        for element in link[target]:
            if element not in dist:
                dist[element] = dist[target] + 1
            queue.append(element)

    return dist[dest]


def is_diff_only_one(word1, word2):
    diff = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            diff += 1

    return True if diff == 1 else False


def solution(begin, target, words):
    answer = 0
    if target not in words:
        return answer

    # make link
    link = {}
    for word in words + [begin]:
        link[word] = []
        for i in range(len(words)):
            if is_diff_only_one(word, words[i]):
                link[word].append(words[i])

    print(link)

    return bfs(link, begin, target)

if __name__ == '__main__':
    print(solution('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']))