from sys import stdin
read = lambda: stdin.readline().split()


def upside_down(chunk):
    if len(chunk) == 4:
        return chunk[2] + chunk[3] + chunk[0] + chunk[1]
    else:
        print(chunk)


def find_chunk(tree):
    chunk = []
    for i in range(len(tree)):
        if len(chunk) == 4:
            break
        else:
            if tree[i] == 'x':
                sub_chunk = find_chunk(tree[i+1:])
                for j in range(len(sub_chunk)):
                    tree[i+j] = 0
                chunk.append(sub_chunk)
            elif tree[i] == 0:
                pass
            else:
                chunk.append(tree[i])
    chunk = upside_down(chunk)
    return 'x' + chunk


C = int(input())

for _ in range(C):
    tree = read()
    tree = [t for t in tree[0]]
    if tree[0] == 'w' or tree[0] == 'b':
        print(tree[0])
    else:
        tree = find_chunk(tree[1:])
        print(tree)
