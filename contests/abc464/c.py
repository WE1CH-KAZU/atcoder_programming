import sys
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from heapq import heappop, heappush
from itertools import (
    combinations,
    permutations,  # 順列組み合わせ
)

input = sys.stdin.readline

INF = 10**18
MOD = 998244353


# N 鳥の数
# M 観察した日数
N, M = map(int, input().split())

cnt = Counter()

# d日目の変化を入れる
events = [
    [] for _ in range(M+1)
]
for _ in range(1,N+1):
    A, D, B = map(int, input().split())
    cnt[A] +=1 # 色をカウントアップ
    events[D].append((A,B)) # イベント内容を一旦保存

# 色の数
kinds = len(cnt)

ans = []
for i in range(1, M+1):
    for A, B in events[i]:
        cnt[A] -= 1
        if cnt[A] == 0:
            #色がなくなったら
            kinds -= 1
        if cnt[B] == 0:
            #色が追加されたら
            kinds += 1
        cnt[B] += 1

    ans.append(kinds)

print('\n'.join(map(str, ans)))
