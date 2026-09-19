import sys
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from heapq import heappop, heappush
from itertools import (
    combinations,
    permutations,  # 順列組み合わせ
)

input = sys.stdin.readline
# 再起上限
sys.setrecursionlimit(10**6)

INF = 10**18
MOD = 998244353

def sosu_judge(n):
    # 素数かどうかを判定する
    if n < 2:
        return False
    for d in range(2, int(n ** 0.5)+ 1):
        if n % d ==0:
            return False
    return True

T = int(input())

ans =[]
for t in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    yugrid = ((x2-x1)**2 + (y2-y1)**2)
    if (r1 - r2)**2 <= yugrid <= (r1+r2)**2:
        ans.append("Yes")
    else:
        ans.append("No")

print("\n".join(ans))
