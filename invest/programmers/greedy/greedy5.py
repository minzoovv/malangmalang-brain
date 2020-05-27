def get_parent(n, cycle):
    if n == cycle[n]:
        return n
    else:
        return get_parent(cycle[n], cycle)


def have_same_parent(n, m, cycle):
    p_n, p_m = get_parent(n, cycle), get_parent(m, cycle)
    return True if p_n == p_m else False


def make_union(n, m, cycle):
    p_m = get_parent(m, cycle)
    cycle[p_m] = get_parent(n, cycle)


# 크루스칼 알고리즘
def solution(n, costs):
    costs = sorted(costs, key=lambda a: a[2])
    cycle = [i for i in range(n)]  # 사이클 테이블이 꼭 필요하다
    answer = 0

    for cost in costs:
        node1, node2, c = cost
        if have_same_parent(node1, node2, cycle):
            continue

        make_union(node1, node2, cycle)
        answer += c

        if all(cycle[i] == cycle[i - 1] for i in range(1, len(cycle))):
            break

    return answer