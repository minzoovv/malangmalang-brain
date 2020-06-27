import sys
input = sys.stdin.readline
# print = sys.stdout.write

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]


def find(a):
    p = parent[a]
    if p == a:
        return a
    else:
        parent[a] = find(p)  # 이렇게 한번 갱신해주는게 효율적이다
        return parent[a]


def union(a, b):
    a_p, b_p = find(a), find(b)
    if a_p != b_p:
        parent[b_p] = a_p


for _ in range(m):
    ops, num1, num2 = map(int, input().split())
    if ops == 0:
        union(num1, num2)
    elif ops == 1:
        value = 'YES' if find(num1) == find(num2) else 'NO'
        print(value)
