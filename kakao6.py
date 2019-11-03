from itertools import permutations


def check_fixable(n, members, weak):
    for i in range(len(weak)):
        linear_dist = get_linear_dist(n, weak, i)
        for member in members:
            coverage = linear_dist[0] + member
            # can cover all
            if coverage >= linear_dist[len(linear_dist)-1]:
                linear_dist = []
                break

            else:
                for j in range(len(linear_dist)):
                    if coverage < linear_dist[j]:
                        linear_dist = linear_dist[j:]
                        break

        if not linear_dist:
            return True

    return False


def get_linear_dist(n, weak, start_idx):
    linear_dist = []
    for i in range(start_idx, len(weak)):
        linear_dist.append(weak[i])

    for i in range(0, start_idx):
        linear_dist.append(weak[i] + n)

    return linear_dist


def solution(n, weak, dist):
    answer = -1
    dist.sort(reverse=True)
    for i in range(0, len(dist)):
        members_p = list(permutations(dist[0:i+1]))
        for members in members_p:
            members = list(members)

            if check_fixable(n, members, weak):
                answer = len(members)
                return answer

    return answer

print(solution(200, [1, 3, 5, 6, 7, 8, 9, 11, 13, 14, 15, 16, 18, 20, 22], [1,1,1,1,1,1,2,2]))