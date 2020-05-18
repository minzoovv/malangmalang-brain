
def dfs(tickets, idx, visited, route, route_list):
    ticket = tickets[idx]  # 해당 ticket의 정보를 가져옴
    visited[idx] = 1  # 해당 ticket의 사용 표시

    # 내가 다음 곳으로 갈 필요가 있나? 목적지를 다했나?

    if len(route) == len(tickets):
        # 전부 ticket을 소진함
        route_list.append(route + [ticket[1]])
        return

        # 티켓을 소비하지 않았음, 그러면 갈 곳이 있는지 체크해야함
    next = []
    for i in range(len(tickets)):
        # 다음에 갈 수 있는 곳을 전부 가져옴
        if ticket[1] == tickets[i][0] and visited[i] == 0:
            next.append(i)

    if next:
        # 갈 곳이 있음.
        for n in next:
            new_route = route + [tickets[n][0]]
            dfs(tickets, n, visited, new_route, route_list)

    else:
        # 갈 곳이 없음
        visited[idx] = 0
        route.pop()
        return


def solution(tickets):
    route_list = []

    for i in range(len(tickets)):
        visited = [0 for _ in range(len(tickets))]
        if tickets[i][0] == "ICN":
            dfs(tickets, i, visited, ["ICN"], route_list)

    # print(route_list)

    return min(route_list)

# route list를 받아야하고,
# 해당 ticket를 전부 사용하는 시점에 해당 여태 왔던 route를 route list에 넣고 끝내야 한다
# 그렇지 않거나, 더이상 소비할 수 없는 상황이면 리턴하고 끝내야함
# 결국 남는건 route_list
# 해당 ticket를 사용했다는 것을 체크해줘야함, 해당 scope에 머물러 있어야 함.
# entry point가 모든 ICN에서 시작하는 ticket, 그리고 해당 ticket 다음에 갈 곳이 없으면 그냥 끝내야함


# best solution

from collections import defaultdict


# def dfs(graph, N, key, footprint):
#     print(footprint)
#     # 모든 ticket을 다 사용했을 때 이렇게 그대로 return을 해준다.
#     if len(footprint) == N + 1:
#         return footprint
#
#     for idx, country in enumerate(graph[key]):
#         graph[key].pop(idx)
#
#         # 아예 새로운 footprint 선언. 나의 new_route와 동일함
#         tmp = footprint[:]
#         tmp.append(country)
#
#         ret = dfs(graph, N, country, tmp)
#
#         # 다시 해당 방문을 graph에 넣어준다. restore하는 방식
#         graph[key].insert(idx, country)
#
#         # return 값이 존재할 때만 진행해준다
#         if ret:
#             return ret


# 해당 그래프가 갈 곳이 없으면 저절로 return None이 되어 무시가 된다.

# def solution(tickets):
#     answer = []
#     # 신박한 defaultdict! 전부 list로 초기값이 초기화 된다. 완전 좋다.
#     graph = defaultdict(list)
#
#     N = len(tickets)
#     for ticket in tickets:
#         graph[ticket[0]].append(ticket[1])
#         # 이렇게 그래프를 만들고 sorting해주었다. 내가 처음 시도했던 방법.
#         graph[ticket[0]].sort()
#
#
# answer = dfs(graph, N, "ICN", ["ICN"])
#
# return answer

if __name__ == '__main__':
    print(solution(tickets=[["ICN", "SFO"], ["ICN", "ATL"], ["ATL", "ICN"], ["ICN", "ZEN"], ["ZEN", "ICN"], ["SFO", "ICN"], ["ICN", "SFO"]]
))