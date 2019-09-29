from sys import stdin
read = lambda: stdin.readline().strip()


def check_possibility(pattern, file_name):
    # get cache to the result
    if not pattern and not file_name:
        return True
    elif not pattern and file_name:
        return False
    else:
        ans = cache.get((pattern[0], file_name))
        if ans:
            return ans
        else:
            if pattern[0] == '*':
                if len(pattern) == 1:
                    ans = True
                    pass
                else:
                    if file_name:
                        for i in range(len(file_name)):
                            ans = check_possibility(pattern[1:], file_name[i:])
                            if ans is True:
                                break
                    else:
                        if all(i == '*' for i in pattern):
                            ans = True
                        else:
                            ans = False
            elif pattern[0] == '?':
                ans = check_possibility(pattern[1:], file_name[1:])
            else:
                if pattern[0] == file_name[0]:
                    ans = check_possibility(pattern[1:], file_name[1:])
                else:
                    ans = False

        # memoization
        cache[(pattern[0], file_name)] = ans
        return ans


for _ in range(int(input())):
    # get pattern
    pattern = [i for i in map(str, read())]
    cache = {}
    results = []
    for _ in range(int(input())):
        file_name = read()
        if check_possibility(pattern, file_name):
            results.append(file_name)
        else:
            pass

    # sorting
    results.sort()
    for result in results:
        print(result)

# nonzero return code - need to fix caching way