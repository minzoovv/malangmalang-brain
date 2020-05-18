def allocate(lost, reserve):
    '''allocate reserve to lost, return non allocator'''
    if not lost:
        return lost

    for r in reserve:
        candidate = {r + 1, r - 1}
        borrower = list(candidate & set(lost))
        if borrower:
            lost.remove(borrower[0])
    return lost


def solution(n, lost, reserve):
    # 선작업
    duplicate = set(lost) & set(reserve)
    lost = list(set(lost) ^ duplicate)
    reserve = list(set(reserve) ^ duplicate)

    non_allocator = allocate(lost, reserve)

    return n - len(non_allocator)