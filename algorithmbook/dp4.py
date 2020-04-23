from sys import stdin, stdout
read = lambda: stdin.readline().split()

C = int(input())


def jlis(indexA, indexB):
    ret = 0
    a = -1 if indexA == -1 else seq1[indexA]
    b = -1 if indexB == -1 else seq2[indexB]
    max_element = max(a, b)

    if dp[indexA+1][indexB+1] != -1:
        return dp[indexA+1][indexB+1]

    for i in range(indexA+1, n):
        if max_element < seq1[i]:
            ret = max(ret, jlis(i, indexB) + 1)

    for j in range(indexB+1, m):
        if max_element < seq2[j]:
            ret = max(ret, jlis(indexA, j) + 1)

    dp[indexA+1][indexB+1] = ret
    return ret


for _ in range(C):
    n, m = map(int, read())
    dp = [[-1 for _ in range(m+1)] for _ in range(n+1)]
    seq1 = [i for i in map(int, read())]
    seq2 = [i for i in map(int, read())]
    print(jlis(-1, -1))
