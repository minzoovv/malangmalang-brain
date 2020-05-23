def solution(people, limit):
    people = sorted(people)

    if len(people) == 1:
        return 1
    if len(people) == 2:
        return 2 if sum(people) > limit else 1

    answer, end = 0, 0
    i, j = 0, len(people) - 1

    while i < j:
        smallest, biggest = people[i], people[j]
        if smallest + biggest <= limit:
            i += 1
            j -= 1
            end = 0
        else:
            j -= 1
            end = 1
        answer += 1

    if (i == j and end == 0) or end == 1:
        answer += 1

    return answer