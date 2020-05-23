def dp(triangle, mem, height):
    line = triangle[height]
    for i in range(len(line)):
        if i == 0:
            mem[height][i] = mem[height-1][i] + line[i]
        elif i == len(line)-1:
            mem[height][i] = mem[height-1][i-1] + line[i]
        else:
            mem[height][i] = max(mem[height-1][i-1], mem[height-1][i]) + line[i]


def solution(triangle):
    mem = [[-1 for i in range(len(t))] for t in triangle]
    mem[0][0] = triangle[0][0]
    for i in range(1, len(triangle)):
        dp(triangle, mem, i)
    return max(mem[len(triangle)-1])
