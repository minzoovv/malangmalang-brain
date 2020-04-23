# from functools import lru_cache
from sys import stdin
read = lambda: stdin.readline().split()


# @lru_cache
def check_possibility(y, x, size: int):
    if y > (size-1) or x > (size-1):
        return 0
    if y == (size-1) and x == (size-1):
        return 1

    step = board[y][x]
    if dp[y][x] != -1:
        return dp[y][x]
    else:
        dp[y][x] = check_possibility(y+step, x, size) or check_possibility(y, x+step, size)
        return dp[y][x]


C = int(input())
for _ in range(C):
    size = int(input())
    dp = [[-1 for _ in range(size)] for _ in range(size)] # check yes or no
    board = [[i for i in map(int, read())] for _ in range(size)]
    print("YES" if check_possibility(0, 0, size) else "NO")

