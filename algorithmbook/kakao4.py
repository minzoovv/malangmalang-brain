def check_expression(words, query, cache):
    # 일단 기본적으로 길이 체크?
    # caching을 무조건적으로 해줘야함
    result = 0
    if query in cache.keys():
        return cache[query]
    for word in words:
        if len(query) != len(word):
            continue
        else:
            if query.count('?') == len(query):
                result += 1
            else:
                if query.index('?') == 0:
                    end_index = query.count('?')
                    if query[end_index:] == word[end_index]:
                        result += 1
                else:
                    index = query.index('?')
                    if query[0:index] == word[0:index]:
                        result += 1
    return result


def solution(words, queries):
    tries = [({}, {}) for _ in range(10001)]  # by length

    for word in words:
        trie = tries[len(word)][0]
        for c in word:
            trie['count'] = trie.get('count', 0) + 1
            trie.setdefault(c, {})
            trie = trie[c]
        trie = tries[len(word)][1]

        for c in word[::-1]:
            trie['count'] = trie.get('count', 0) + 1
            trie.setdefault(c, {})
            trie = trie[c]

    answer = []
    for query in queries:
        if query[0] == '?':
            t = tries[len(query)][1]
            query = query[::-1]
        else:
            t = tries[len(query)][0]
        for c in query:
            if c == '?':
                answer.append(t.get('count', 0))
                break
            if c not in t:
                answer.append(0)
                break
            t = t[c]
    return answer


result = solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"])
print(result)