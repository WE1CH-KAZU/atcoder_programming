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

Q = int(input())
S = input().strip()
T = input().strip()

# 最初に全部確認
pos_t = []
t =S.find(T)

while t != -1:
    pos_t.append(t)
    t = S.find(T, t+1)

t_nagasa = len(T)
ans = []

# 長さ判定
for i in range(Q):
    L, R = map(int, input().split())
    hajime = bisect_left(pos_t, L-1)
    if hajime < len(pos_t) and pos_t[hajime] + t_nagasa <= R:
        ans.append('Yes')
    else:
        ans.append("No")

print("\n".join(ans))
