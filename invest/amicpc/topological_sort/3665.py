test_case = int(input())

# topological sort는 진입차수가 중요하다.
# team1이 team2 보다 높은 등수로 되었다.
# 과거의 것으로 봤을 때, 어떤 차이가 있지?
# 5 <- 4 <- 3 <- 2 <- 1
# 수가 바뀌었다면, 그게 뭘 의미하는걸까 위상정렬에서는?
# 이런 위상정렬에서 2, 4가 들어왔다면?
# 2가 4를 앞선다
# 3이 4를 앞선다
# 하지만 2와 3은 바뀌지 않았어
# 이를 통해서
# 2 <- 4 가 되려면 3 <- 4도 같이 선행되어야 하네


# 1 <- 2 <- 3 <- 4
# 2 1을 앞선다
# 4 3
# 2 3
# 4 <- 3 <- 2 <- 1 근데 4랑 1은 안바꼈으니까 IMPOSSIBLE
#
# 위의 경우엔...

for _ in range(test_case):
    n = int(input())
    last_year = list(map(int, input().split()))
    changed = []

    m = int(input())
    for _ in range(m):
        team1, team2 = input().split()
        changed.append((team1, team2))
        # team 1이 team2 보다 순위가 높아졌다.



