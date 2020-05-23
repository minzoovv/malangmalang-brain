from math import inf

mod_val = 1000000007

dx = [-1, 0]
dy = [0, -1]


def dp(mem, y, x):
    if mem[y][x] != 0:
        return mem[y][x]

    prev = [mem[y + dy[0]][x + dx[0]], mem[y + dy[1]][x + dx[1]]]
    for p in prev:
        if p != inf:
            mem[y][x] += p

    return mem[y][x]


def solution(m, n, puddles):
    mem = [[inf] * int(m + 1)]
    for i in range(0, n):
        mem.append([inf] + [0 for _ in range(m)] + [inf])
    mem.append([inf] * int(m + 1))

    mem[1][1] = 1

    for x, y in puddles:
        mem[y][x] = inf

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp(mem, i, j)

    answer = mem[n][m]
    return answer % mod_val