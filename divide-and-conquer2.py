from sys import stdin
read = lambda: stdin.readline().split()


def find_max_area(lengths: list):
    if len(lengths) <= 0:
        return 0
    elif len(lengths) == 1:
        return lengths[0]
    else:
        shortest = min(lengths)
        index = lengths.index(shortest)

        return max(find_max_area(lengths[0:index]),
                   find_max_area(lengths[index+1:]),
                   shortest * len(lengths))


C = int(input())

for _ in range(C):
    wood = int(input())
    lengths = list(map(int, read()))
    result = find_max_area(lengths)
    print(result)

# i dont know why but it doesn't work in algospot
