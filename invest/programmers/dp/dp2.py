def dp(mem, count):
    if count == 1:
        return mem[1][1]

    if mem[count][1] != 0:
        return mem[count][1]

    mem[count][0] = mem[count-1][0] + mem[count-2][0]
    mem[count][1] = dp(mem, count-1) + mem[count][0] * 2

    print(mem)
    return mem[count][1]


def solution(N):
    mem = [[0, 0] for _ in range(N + 1)]
    mem[1] = [1, 4]
    mem[2][0] = 1
    for i in range(3, N+1):
        dp(mem, i)

    return mem[N][1]


if __name__ == '__main__':
    print(solution(6))