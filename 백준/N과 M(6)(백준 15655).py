import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
choose = [0 for _ in range(10)]
used = [0] * 10
arr = sorted(list(map(int, input().split())))


def dfs(depth, i):
    if depth == M:
        for idx in range(depth):
            print(arr[choose[idx]], end = " ")
        print()
        return
    for i in range(i, N):
        if used[i]:
            continue
        used[i] = 1
        choose[depth] = i
        dfs(depth + 1, i + 1)
        used[i] = 0
dfs(0, 0)