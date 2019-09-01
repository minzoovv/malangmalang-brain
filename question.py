def tester():
    f = open("./questions.txt", "rt")
    case_count = f.readline()

    for i in range(int(case_count)):
        n_m = f.readline().strip()
        friends_pair = f.readline().strip()

        n_m = n_m.split(' ')
        friends_pair = friends_pair.split(' ')

        solution(n_m, friends_pair)


def solution(n_m, friends_pair):
    """
    Write your answer here!!
    :param n_m:
    :param friends_pair:
    :return:
    """
    pass


def main():
    tester()


if __name__ == '__main__':
    main()
