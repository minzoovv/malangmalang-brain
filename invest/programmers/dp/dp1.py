def dp(N, number, s):
    # 해당 연산 값이 있는지 계산
    for i in range(2, 9):
        s.append({int(str(N) * i)})
        if int(str(N) * i) == number:
            return i

        for j in range(1, i):
            N_num = int(str(N) * j)
            for value in s[i - j]:
                result_val = {N_num + value,
                              N_num - value,
                              value - N_num,
                              N_num * value,
                              value // N_num}
                if value != 0:
                    result_val.add(N_num // value)
                s[i] = s[i].union(result_val)

        if number in s[i]:
            return i
    else:
        return -1


def solution(N, number):
    # # s라는 list -> 이는 모든 가능한 number값을 갖고 있다
    # S = [{N}]  # 1일때를 의미
    # for i in range(2, 9):
    #     # 이 i가 최소 수를 의미
    #     lst = [int(str(N) * i)]
    #     # 5~5*i 까지의 모둔 5가 되는 수를 미리 만듬
    #     for X_i in range(0, int(i / 2)):
    #         # 가능한 연 산 수는 5를 붙인 것 나누기 2
    #         for x in S[X_i]:
    #             # 각 s안의 값, 0~i/2까지
    #             print(i - X_i - 2)
    #             for y in S[i - X_i - 2]:
    #                 # 그리고 각 s안의
    #                 lst.append(x + y)
    #                 lst.append(x - y)
    #                 lst.append(y - x)
    #                 lst.append(x * y)
    #                 if x != 0: lst.append(y // x)
    #                 if y != 0: lst.append(x // y)
    #     if number in set(lst):
    #         print(set(lst))
    #         return i
    #     S.append(lst)
    #     print(S)
    # return -10
    s = [{-1}, {N}]
    answer = dp(N, number, s)
    return answer

if __name__ == '__main__':
    print(solution(5, 12))
