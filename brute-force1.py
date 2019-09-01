from sys import stdin, stdout
read = lambda: stdin.readline().split()


def match_case(friends, people):
    init = 0
    if not people:
        return 1
    else:
        p1 = people.pop(0)
        for p2 in people:
            if (p1, p2) in friends or (p2, p1) in friends:
                rest = people.copy()
                rest.remove(p2)
                init += match_case(friends, rest)
            else:
                pass
        return init


C = int(input())
for _ in range(C):
    N, M = map(int, read())
    temp = list(map(int, read()))
    friends = [(temp[i], temp[i+1]) for i in range(0, len(temp), 2)]

    result = match_case(friends, [i for i in range(N)])
    print(result)




