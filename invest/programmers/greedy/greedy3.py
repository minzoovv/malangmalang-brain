def greedy(number, k):
    increase = []
    idx = 0
    #     while idx < len(number)-1:
    #         if number[idx] > number[idx+1]:
    #             phase = 1
    #             idx += 1
    #             break
    #         elif number[idx] < number[idx+1]:
    #             phase = 2
    #             break
    #         idx += 1

    #     if phase == 2:
    #         number.pop(idx)
    #         return

    while k != 0 and idx < len(number) - 1:
        if number[idx] > number[idx + 1]:
            if not increase:
                increase.append(idx)
        elif number[idx] < number[idx + 1]:
            number = number[:idx] + number[idx + 1:]
            if increase:
                print(k, increase, number)
                idx = increase[0]
                increase = []
            k -= 1
            continue
        idx += 1
    return number[:-k] if k else number


def solution(number, k):
    # number_list = []
    # for n in number:
    #     number_list.append(int(n))
    number = greedy(number, k)
    return number


def greedy(number, k):
    increase = None
    idx = 0
    #     while idx < len(number)-1:
    #         if number[idx] > number[idx+1]:
    #             phase = 1
    #             idx += 1
    #             break
    #         elif number[idx] < number[idx+1]:
    #             phase = 2
    #             break
    #         idx += 1

    #     if phase == 2:
    #         number.pop(idx)
    #         return

    while k != 0 and idx < len(number) - 1:
        if number[idx] > number[idx + 1]:
            if increase is None:
                increase = idx
        elif number[idx] < number[idx + 1]:
            number = number[:idx] + number[idx + 1:]
            k -= 1
            if increase is not None:
                idx = increase
                increase = None
            continue
        idx += 1
    return number[:-k] if k else number


def solution(number, k):
    # number_list = []
    # for n in number:
    #     number_list.append(int(n))
    number = greedy(number, k)
    return number