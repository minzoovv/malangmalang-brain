import sys


def dp(steps, result, n):
    if result[n] != 0:
        return

    if n == 2:
        result[n] = max(steps[n] + result[n - 2], steps[n] + steps[n - 1])
        # n은 2일 경우 n-3이 존재하지 않으므로, 이런 식으로 핸들링 필요
        return

    result[n] = max(steps[n] + result[n - 2], steps[n] + steps[n - 1] + result[n - 3])
    # 이 과정에서 n-3의 result를 부름으로써 2개 연속의 step이 없도록 한다


n = int(input())
steps = []
for _ in range(n):
    steps.append(int(input()))

result = [0 for i in range(n)]
result[0] = steps[0]
if n == 1:
    print(steps[0])
    sys.exit()  # 1일 때를 체크해주어야 한

result[1] = max(steps[0] + steps[1], steps[0])

for i in range(2, n):
    dp(steps, result, i)

print(result[n - 1])
