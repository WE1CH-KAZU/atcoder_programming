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

# N=本数
# X=座席番号
N, X = input().split()
N = int(N)
X = 'ABCDE'.index(X)

# zaseki = {
#     'A': 0,
#     'B': 1,
#     'C': 2,
#     'D': 3,
#     'E': 4,
# }
# X = zaseki[X]

# ans = 0
# for i in range(1, N+1):
#     S = list(input().strip())
#     if S[X] == 'o':
#         ans += INF
#     else:
#         ans -= 1

# if ans > 0:
#     print('Yes')
# else:
#     print('No')


# ========
# 上記でも良いが、もっとシンプルにかける

ans = False

for _ in range(N):
    S = input().strip()
    if S[X] == 'o':
        ans = True
        break

print(
    'Yes' if ans else 'No'
)
