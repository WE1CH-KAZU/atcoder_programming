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

X, Y, L, R, A, B = map(int, input().split())

if A < B <= L or R <= A < B:
    # 範囲外
    time = B - A
    print(Y*time)
elif L <= A < B <= R:
    # 範囲内
    time = B - A
    print(X*time)
elif A <= L < R <= B:
    # 両側へはみ出ている
    time1 = L - A
    time2 = R - L
    time3 = B - R
    print((time1+time3)*Y+time2*X)
elif A <= L < B:
    # 左側へはみ出ている
    time1 = L - A
    time2 = B - L
    print(time1*Y+time2*X)
elif A < R <= B:
    # 右側へはみ出ている
    time1 = B - R
    time2 = R - A
    print(time1*Y+time2*X)
