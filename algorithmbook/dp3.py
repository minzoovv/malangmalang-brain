from sys import stdin, stdout
read = lambda: stdin.readline().split()

C = int(input())

for _ in range(C):
    n = int(input())
    dp = [0 for _ in range(n+1)]
    seq = [0] + [i for i in map(int, read())]

    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = 1
        for j in range(1, i):
            if seq[j] < seq[i]:
                dp[i] = max(dp[i], dp[j]+1)

    print(max(dp))
